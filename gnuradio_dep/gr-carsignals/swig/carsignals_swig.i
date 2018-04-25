/* -*- c++ -*- */

#define CARSIGNALS_API

%include "gnuradio.i"			// the common stuff

//load generated python docstrings
%include "carsignals_swig_doc.i"

%{
#include "carsignals/carsignal_sink.h"
%}


%include "carsignals/carsignal_sink.h"
GR_SWIG_BLOCK_MAGIC2(carsignals, carsignal_sink);
