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


#ifndef INCLUDED_RENOMALY_SNR_ACCUMULATOR_H
#define INCLUDED_RENOMALY_SNR_ACCUMULATOR_H

#include <ReNoMalY/api.h>
#include <gnuradio/block.h>

namespace gr {
  namespace ReNoMalY {

    /*!
     * \brief <+description of block+>
     * \ingroup ReNoMalY
     *
     */
    class RENOMALY_API SNR_Accumulator : virtual public gr::block
    {
     public:
      typedef boost::shared_ptr<SNR_Accumulator> sptr;

      /*!
       * \brief Return a shared_ptr to a new instance of ReNoMalY::SNR_Accumulator.
       *
       * To avoid accidental use of raw pointers, ReNoMalY::SNR_Accumulator's
       * constructor is in a private implementation
       * class. ReNoMalY::SNR_Accumulator::make is the public interface for
       * creating new instances.
       */
      static sptr make(size_t vlen);
    };

  } // namespace ReNoMalY
} // namespace gr

#endif /* INCLUDED_RENOMALY_SNR_ACCUMULATOR_H */

