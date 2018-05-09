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

#ifndef INCLUDED_CARSIGNALS_CARSIGNAL_SINK_IMPL_H
#define INCLUDED_CARSIGNALS_CARSIGNAL_SINK_IMPL_H

#include <carsignals/carsignal_sink.h>

namespace gr {
  namespace carsignals {

    class carsignal_sink_impl : public carsignal_sink
    {
     private:
      size_t d_itemsize;

     public:
      carsignal_sink_impl(size_t itemsize, std::string filepath, std::string initFreq);
      ~carsignal_sink_impl();

      void set_frequency(std::string curr_freq);
      
      // Where all the action really happens
      int work(int noutput_items,
         gr_vector_const_void_star &input_items,
         gr_vector_void_star &output_items);
    };

  } // namespace carsignals
} // namespace gr

#endif /* INCLUDED_CARSIGNALS_CARSIGNAL_SINK_IMPL_H */

