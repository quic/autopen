/* -*- c++ -*- */
/* 
 * Copyright 2018 <+YOU OR YOUR COMPANY+>.
 * 
 * This is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 3, or (at your option)
 * any later version.
 * 
 * This software is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this software; see the file COPYING.  If not, write to
 * the Free Software Foundation, Inc., 51 Franklin Street,
 * Boston, MA 02110-1301, USA.
 */

#ifdef HAVE_CONFIG_H
#include "config.h"
#endif

#include <gnuradio/io_signature.h>
#include "carsignal_sink_impl.h"

namespace gr {
  namespace carsignals {

    std::string currentFrequency = "315";
    std::string currentopen = "0";
    std::string basepath;

    carsignal_sink::sptr
    carsignal_sink::make(size_t itemsize, std::string filepath, std::string initFreq)
    {
      return gnuradio::get_initial_sptr
        (new carsignal_sink_impl(itemsize, filepath, initFreq));
    }

    /*
     * The private constructor
     */
    carsignal_sink_impl::carsignal_sink_impl(size_t itemsize, std::string filepath, std::string initFreq)
      : gr::sync_block("carsignal_sink",
              gr::io_signature::make(1, 1, itemsize),
              gr::io_signature::make(0, 0, 0)),
      file_sink_base(  (filepath+initFreq).c_str() , true, true),
      d_itemsize(itemsize)
    {
      set_unbuffered(false);
      basepath = filepath;
      currentopen = initFreq;
      currentFrequency = initFreq;
      //open((basepath+currentFrequency).c_str());
    }

    /*
     * Our virtual destructor.
     */
    carsignal_sink_impl::~carsignal_sink_impl()
    {
    }

    void 
    carsignal_sink_impl::set_frequency(std::string curr_freq){
      currentFrequency = curr_freq;
    }

    int
    carsignal_sink_impl::work(int noutput_items,
        gr_vector_const_void_star &input_items,
        gr_vector_void_star &output_items)
    {
      //if(currentopen == "z_drop"){
      //  return noutput_items;
      //}

      if(currentFrequency != currentopen){ //if the file that is open doesnt match the frequency we retuned.
        close();
        open((basepath+currentFrequency).c_str());
        currentopen = currentFrequency;
      }

      char *inbuf = (char*)input_items[0];
      int  nwritten = 0;

      do_update();                    // update d_fp is reqd

      if(!d_fp)
        return noutput_items;         // drop output on the floor

      while(nwritten < noutput_items) {
        int count = fwrite(inbuf, d_itemsize, noutput_items - nwritten, d_fp);
        if(count == 0) {
          if(ferror(d_fp)) {
            std::stringstream s;
            s << "file_sink write failed with error " << fileno(d_fp) << std::endl;
            throw std::runtime_error(s.str());
          }
          else { // is EOF
            break;
          }
        }
        nwritten += count;
        inbuf += count * d_itemsize;
      }

      if(d_unbuffered)
        fflush (d_fp);

      return nwritten;
    
    }
  } /* namespace carsignals */
} /* namespace gr */

