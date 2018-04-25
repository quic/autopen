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
#include "SNR_AVG_impl.h"
#define SAMPLE_NUM 8
namespace gr {
  namespace ReNoMalY {

    SNR_AVG::sptr
    SNR_AVG::make(size_t vlen)
    {
      return gnuradio::get_initial_sptr
        (new SNR_AVG_impl(vlen));
    }

    /*
     * The private constructor
     */
    SNR_AVG_impl::SNR_AVG_impl(size_t vlen)
      : gr::block("SNR_AVG",
              gr::io_signature::make(1, 1, sizeof(float)*vlen),
              gr::io_signature::make(1, 1, sizeof(float))),
		d_vlen(vlen)
    {}

    /*
     * Our virtual destructor.
     */
    SNR_AVG_impl::~SNR_AVG_impl()
    {
    }

    void
    SNR_AVG_impl::forecast (int noutput_items, gr_vector_int &ninput_items_required)
    {
      ninput_items_required[0] = noutput_items;/* */
    }

    int
    SNR_AVG_impl::general_work (int noutput_items,
                       gr_vector_int &ninput_items,
                       gr_vector_const_void_star &input_items,
                       gr_vector_void_star &output_items)
    {
      const float *in = (const float *) input_items[0];
      float *out = (float *) output_items[0];

      // Do <+signal processing+>
 /* 	ARG_MAX LOGIC	 */
		int maxIndex = 0;
		float max = in[0];
		for(int i =1;i<d_vlen;i++){
			if(in[i] > max) maxIndex = i;
		}
		
		float accSound = 0;
		float accNoise = 0;
		
		/*		NOISE SUMS 		*/
		for(int i = 0; i < maxIndex - SAMPLE_NUM +1; i++)
			accNoise += in[i];
		for(int i = maxIndex + SAMPLE_NUM + 1; i<d_vlen; i++)
			accNoise += in[i];
			
		/*		SOUND SUMS		*/
		for(int i = maxIndex-SAMPLE_NUM; i<maxIndex+SAMPLE_NUM; i++)
			accSound += in[i];
			
		float SnR = accSound/accNoise;
		float SnR_db = 10 * std::log10(SnR);
		
		//printf("The output of SNR is %f \n", SnR_db);
		out[0] = SnR_db;
	
      // Tell runtime system how many input items we consumed on
      // each input stream.
      consume_each (noutput_items);

      // Tell runtime system how many output items we produced.
      return noutput_items;
    }

  } /* namespace ReNoMalY */
} /* namespace gr */

