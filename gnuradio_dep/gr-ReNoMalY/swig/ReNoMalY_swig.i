/* -*- c++ -*- */

#define RENOMALY_API

%include "gnuradio.i"			// the common stuff

//load generated python docstrings
%include "ReNoMalY_swig_doc.i"

%{
#include "ReNoMalY/SNR_AVG.h"
#include "ReNoMalY/SNR_Accumulator.h"
#include "ReNoMalY/isAnomaly.h"
%}


%include "ReNoMalY/SNR_AVG.h"
GR_SWIG_BLOCK_MAGIC2(ReNoMalY, SNR_AVG);
%include "ReNoMalY/SNR_Accumulator.h"
GR_SWIG_BLOCK_MAGIC2(ReNoMalY, SNR_Accumulator);
%include "ReNoMalY/isAnomaly.h"
GR_SWIG_BLOCK_MAGIC2(ReNoMalY, isAnomaly);
