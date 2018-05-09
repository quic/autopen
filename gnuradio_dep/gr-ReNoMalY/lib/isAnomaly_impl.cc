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
#include <iostream>
#include <fstream>
#include <string>
#include <cstring>
#include "isAnomaly_impl.h"

namespace gr {
  namespace ReNoMalY {

    isAnomaly::sptr
    isAnomaly::make(size_t vlen, char* file)
    {
      return gnuradio::get_initial_sptr
        (new isAnomaly_impl(vlen, file));
    }

    /*
     * The private constructor
     */
    isAnomaly_impl::isAnomaly_impl(size_t vlen, char* file)
      : gr::block("isAnomaly",
              gr::io_signature::make(1, 2, sizeof(float)),
              gr::io_signature::make(1, 1, sizeof(char))),
		d_vlen(vlen),
		d_file(file)
    {}

    /*
     * Our virtual destructor.
     */
    isAnomaly_impl::~isAnomaly_impl()
    {
    }

    void
    isAnomaly_impl::forecast (int noutput_items, gr_vector_int &ninput_items_required)
    {
      ninput_items_required[0] = 2*noutput_items;/* */
    }

    int
    isAnomaly_impl::general_work (int noutput_items,
                       gr_vector_int &ninput_items,
                       gr_vector_const_void_star &input_items,
                       gr_vector_void_star &output_items)
    {
      const float *in = (const float *) input_items[0];
      char *out = (char *) output_items[0];

      // Do <+signal processing+>
      



      //printf("%s\n","the file is not working." );
      //printf("in 0 is %f\nin 1 is %f", in[0],in[1]);
      float snr_Ratio = in[1]/in[0];
      //printf("\nthe in0/in1 is %f", snr_Ratio);
      //FILE * fd = fopen("/home/josh/autopen2/M2/AutoPen_Recording/Z_Anomaly_Logs.txt","a"); //
      //fprintf(fd, "Writing a file: %s\n", d_file);
      //fclose(fd);


      printf("%s has :%f\n",d_file,snr_Ratio);
    	//this is the old oneeeeee
      //if(snr_Ratio>1.65){//in[1] is baseline
      if(snr_Ratio>1.12){
    		//out[0] = d_file;
       // printf("%s\n", "the car is on fire");
       /* int filesize = sizeof(d_file)/sizeof(d_file);
        for(int i=0;i<filesize;i++)
            out[i]=d_file[i];
       // out[0] = 'a';
        //out[0] = d_file;
        
        //out[0]='a';
        printf("out is this : %c",out[0]);
        printf("out is this : %c",out[1]);
        printf("out is this : %c",out[2]);*/
       /* std::ofstream myfile;
        myfile.open("anomaly_file.txt");
        myfile << "file has anom\n";
        myfile.close();*/
       // std::fstream myfile;
        

       // outputFile.close();
        //std::ofstream myfile;
        //myfile.open();
        //myfile << d_file << std::endl;
        //const char *path = "/home/josh/anomaly_file.txt"; //
        //myfile.open(path);
        
        //myfile << d_file << "\n";
        printf("found anomaly");
        ///home/josh/autopen2/M2/AutoPen_Recording/     Batch_2018-04-10_014-35-25/Batch_2018-04-10_14-35-25_Freq315000000
        std::string zanomFile = std::string(d_file).substr(0,std::string(d_file).find_last_of("/"));
        std::string zanomDir = zanomFile.substr(0,zanomFile.find_last_of("/"));
        printf("outputfile: %s\n",(zanomDir+"/Z_Anomaly.txt").c_str());
        FILE * fd = fopen(   (zanomDir+"/Z_Anomaly.txt").c_str()  ,"a"); //
        fprintf(fd, "%s\n", d_file);
        fclose(fd);
        //fprintf(fd, "%s\n", d_file);
         
         
        /*std::ofstream file(path);
        std::string data(d_file);
        file << data << std::endl;/**/
        //fopen ("/home/josh")
        //out[0]='a';
        //printf("%c\n",out[0] );
        //consume_each (noutput_items);
    		return -1;
    	}
      //printf("\nout is %d",out[0]); ####i commented this linee
      // Tell runtime system how many input items we consumed on
      // each input stream.
      consume_each (noutput_items);

      // Tell runtime system how many output items we produced.
      return noutput_items;
    }

  } /* namespace ReNoMalY */
} /* namespace gr */

