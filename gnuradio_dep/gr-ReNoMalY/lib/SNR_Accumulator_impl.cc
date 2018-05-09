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
#include "SNR_Accumulator_impl.h"

namespace gr {
  namespace ReNoMalY {

    SNR_Accumulator::sptr
    SNR_Accumulator::make(size_t vlen)
    {
      return gnuradio::get_initial_sptr
        (new SNR_Accumulator_impl(vlen));
    }

    /*
     * The private constructor
     */
    SNR_Accumulator_impl::SNR_Accumulator_impl(size_t vlen)
      : gr::block("SNR_Accumulator",
              gr::io_signature::make(1, 1, sizeof(float)*vlen),
              gr::io_signature::make(1, 1, sizeof(float))),
		d_vlen(vlen)
    {}

    /*
     * Our virtual destructor.
     */
    SNR_Accumulator_impl::~SNR_Accumulator_impl()
    {
    }

    void
    SNR_Accumulator_impl::forecast (int noutput_items, gr_vector_int &ninput_items_required)
    {
      ninput_items_required[0] = noutput_items;
    }

    int
    SNR_Accumulator_impl::general_work (int noutput_items,
                       gr_vector_int &ninput_items,
                       gr_vector_const_void_star &input_items,
                       gr_vector_void_star &output_items)
    {
      const float *in = (const float *) input_items[0];
      float *out = (float *) output_items[0];

      // Do <+signal processing+>
	float SnR_acc = 0.0;
	for(int i =0; i<d_vlen; i++){
		SnR_acc += in[i];
	}
	//printf("the value of input is %f and the accumulated is %f\n",in[0],SnR_acc);
	float SnR_avg = SnR_acc / d_vlen;
  //printf("\n\n\nthe Snr avg is %f\n\n\n\n",SnR_avg);
	out[0] =  SnR_avg;
      // Tell runtime system how many input items we consumed on
      // each input stream.
      consume_each (noutput_items);

      // Tell runtime system how many output items we produced.
      return noutput_items;
    }

  } /* namespace ReNoMalY */
} /* namespace gr */

