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


#ifndef INCLUDED_CARSIGNALS_CARSIGNAL_SINK_H
#define INCLUDED_CARSIGNALS_CARSIGNAL_SINK_H

#include <carsignals/api.h>
#include <gnuradio/blocks/file_sink_base.h>
#include <gnuradio/sync_block.h>
#include <string>
#include <unistd.h>

namespace gr {
  namespace carsignals {

    class carsignal_sink;

    /*!
     * \brief <+description of block+>
     * \ingroup carsignals
     *
     */
    class CARSIGNALS_API carsignal_sink : virtual public gr::sync_block, virtual public blocks::file_sink_base
    {
     public:
      typedef boost::shared_ptr<carsignal_sink> sptr;

      /*!
       * \brief Return a shared_ptr to a new instance of carsignals::carsignal_sink.
       *
       * To avoid accidental use of raw pointers, carsignals::carsignal_sink's
       * constructor is in a private implementation
       * class. carsignals::carsignal_sink::make is the public interface for
       * creating new instances.
       */

      static sptr make(size_t itemsize, std::string filepath, std::string initFreq);

      virtual void set_frequency(std::string curr_freq) = 0;
    };

  } // namespace carsignals
} // namespace gr

#endif /* INCLUDED_CARSIGNALS_CARSIGNAL_SINK_H */

