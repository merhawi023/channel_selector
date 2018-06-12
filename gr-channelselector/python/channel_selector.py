#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright 2018 <+YOU OR YOUR COMPANY+>.
# 
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
# 
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
# 

import numpy
from gnuradio import gr

class channel_selector(gr.basic_block):
    """
    docstring for block channel_selector
    """
    def __init__(self, band_size = 32 , start_byte = 0 , end_byte = 31):
        gr.basic_block.__init__(self,
            name="channel_selector",
            in_sig=[numpy.byte],
            out_sig=[numpy.byte])
        self.band_size=band_size
        self.start_byte=start_byte
        self.end_byte=end_byte



    def forecast(self, noutput_items, ninput_items_required):
        #setup size of input_items[i] for work call
        for i in range(len(ninput_items_required)):
            ninput_items_required[i] = noutput_items

    def general_work(self, input_items, output_items):
        
        
        output_counter=0
        for i in range(0 , len(input_items[0])):
            if (i%self.band_size) <= self.start_byte or (i%self.band_size >= self.end_byte):
                pass
            else:
                try:
                    output_items[0][output_counter] =\
                    input_items[0][i]
                except IndexError:
                    pass

                output_counter+=1

        #self.consume_each(len(input_items[0]))
        return len(output_items[0])
