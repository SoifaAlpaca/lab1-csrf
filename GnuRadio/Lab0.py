#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Not titled yet
# GNU Radio version: 3.10.10.0

from PyQt5 import Qt
from gnuradio import qtgui
from PyQt5 import QtCore
from gnuradio import analog
from gnuradio import blocks
from gnuradio import filter
from gnuradio.filter import firdes
from gnuradio import gr
from gnuradio.fft import window
import sys
import signal
from PyQt5 import Qt
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
import sip



class Lab0(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Not titled yet", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Not titled yet")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except BaseException as exc:
            print(f"Qt GUI: Could not set Icon: {str(exc)}", file=sys.stderr)
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "Lab0")

        try:
            geometry = self.settings.value("geometry")
            if geometry:
                self.restoreGeometry(geometry)
        except BaseException as exc:
            print(f"Qt GUI: Could not restore geometry: {str(exc)}", file=sys.stderr)

        ##################################################
        # Variables
        ##################################################
        self.variable_y_freq = variable_y_freq = 250
        self.variable_x_freq = variable_x_freq = 500
        self.variable_m = variable_m = 1
        self.variable_fc = variable_fc = 50000
        self.variable_channel_atenuation = variable_channel_atenuation = 1
        self.variable_a3 = variable_a3 = 0
        self.variable_a2 = variable_a2 = 0
        self.variable_a1 = variable_a1 = 7
        self.samp_rate = samp_rate = 768000

        ##################################################
        # Blocks
        ##################################################

        self._variable_y_freq_range = qtgui.Range(0, 5000, 1, 250, 200)
        self._variable_y_freq_win = qtgui.RangeWidget(self._variable_y_freq_range, self.set_variable_y_freq, "Signal frequency", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._variable_y_freq_win)
        self._variable_x_freq_range = qtgui.Range(0, 5000, 1, 500, 200)
        self._variable_x_freq_win = qtgui.RangeWidget(self._variable_x_freq_range, self.set_variable_x_freq, "Signal frequency", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._variable_x_freq_win)
        self._variable_m_range = qtgui.Range(0, 1, 1, 1, 200)
        self._variable_m_win = qtgui.RangeWidget(self._variable_m_range, self.set_variable_m, "modulation index", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._variable_m_win)
        self._variable_fc_range = qtgui.Range(0, 100000, 1, 50000, 200)
        self._variable_fc_win = qtgui.RangeWidget(self._variable_fc_range, self.set_variable_fc, "central frequency", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._variable_fc_win)
        self._variable_channel_atenuation_range = qtgui.Range(0, 1, 0.01, 1, 200)
        self._variable_channel_atenuation_win = qtgui.RangeWidget(self._variable_channel_atenuation_range, self.set_variable_channel_atenuation, "atenuation", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._variable_channel_atenuation_win)
        self._variable_a3_range = qtgui.Range(-5, 5, 0.1, 0, 200)
        self._variable_a3_win = qtgui.RangeWidget(self._variable_a3_range, self.set_variable_a3, "a3", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._variable_a3_win)
        self._variable_a2_range = qtgui.Range(-10, 10, 1, 0, 200)
        self._variable_a2_win = qtgui.RangeWidget(self._variable_a2_range, self.set_variable_a2, "a2", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._variable_a2_win)
        self._variable_a1_range = qtgui.Range(0, 20, 0.5, 7, 200)
        self._variable_a1_win = qtgui.RangeWidget(self._variable_a1_range, self.set_variable_a1, "a1", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._variable_a1_win)
        self.qtgui_time_sink_x_0_0 = qtgui.time_sink_f(
            1024, #size
            samp_rate, #samp_rate
            "", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_0_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_0.enable_tags(True)
        self.qtgui_time_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_0.enable_autoscale(True)
        self.qtgui_time_sink_x_0_0.enable_grid(False)
        self.qtgui_time_sink_x_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0_0.enable_stem_plot(False)


        labels = ['Signal 1', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_0_win)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_c(
            1024, #size
            samp_rate, #samp_rate
            "", #name
            3, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0.enable_tags(True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(True)
        self.qtgui_time_sink_x_0.enable_grid(False)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0.enable_stem_plot(False)


        labels = ['Signal 1', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(6):
            if len(labels[i]) == 0:
                if (i % 2 == 0):
                    self.qtgui_time_sink_x_0.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_0.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_win)
        self.qtgui_freq_sink_x_0_0 = qtgui.freq_sink_f(
            1024, #size
            window.WIN_FLATTOP, #wintype
            0, #fc
            samp_rate, #bw
            "", #name
            1,
            None # parent
        )
        self.qtgui_freq_sink_x_0_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0_0.set_y_axis((-140), 10)
        self.qtgui_freq_sink_x_0_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_0.enable_autoscale(True)
        self.qtgui_freq_sink_x_0_0.enable_grid(False)
        self.qtgui_freq_sink_x_0_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0_0.enable_control_panel(False)
        self.qtgui_freq_sink_x_0_0.set_fft_window_normalized(False)


        self.qtgui_freq_sink_x_0_0.set_plot_pos_half(not True)

        labels = ['original_cosine_signal', 'original_sine_signal', 'processed_cosine_signal', 'processed_sine_signal', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_0_0_win)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
            1024, #size
            window.WIN_RECTANGULAR, #wintype
            0, #fc
            samp_rate, #bw
            "", #name
            3,
            None # parent
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis((-140), 10)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(True)
        self.qtgui_freq_sink_x_0.enable_grid(False)
        self.qtgui_freq_sink_x_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)
        self.qtgui_freq_sink_x_0.set_fft_window_normalized(False)



        labels = ['original_cosine_signal', 'original_sine_signal', 'processed_cosine_signal', 'processed_sine_signal', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(3):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_0_win)
        self.low_pass_filter_0_0 = filter.interp_fir_filter_ccf(
            1,
            firdes.low_pass(
                1,
                samp_rate,
                (2*variable_x_freq),
                variable_x_freq,
                window.WIN_HAMMING,
                6.76))
        self.low_pass_filter_0 = filter.interp_fir_filter_ccf(
            1,
            firdes.low_pass(
                1,
                samp_rate,
                (2*variable_x_freq),
                variable_x_freq,
                window.WIN_HAMMING,
                6.76))
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_multiply_xx_0_3_1 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_0_3_0_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_0_3_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_0_3 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_0_0_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_0_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_const_vxx_3_0 = blocks.multiply_const_ff(variable_m)
        self.blocks_multiply_const_vxx_3 = blocks.multiply_const_ff(variable_m)
        self.blocks_multiply_const_vxx_2_0 = blocks.multiply_const_cc(variable_a3)
        self.blocks_multiply_const_vxx_2 = blocks.multiply_const_cc(variable_a3)
        self.blocks_multiply_const_vxx_1_1 = blocks.multiply_const_cc(variable_a2)
        self.blocks_multiply_const_vxx_1_0 = blocks.multiply_const_cc(variable_channel_atenuation)
        self.blocks_multiply_const_vxx_1 = blocks.multiply_const_cc(variable_a2)
        self.blocks_multiply_const_vxx_0_0 = blocks.multiply_const_cc(variable_a1)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_cc(variable_a1)
        self.blocks_float_to_complex_1 = blocks.float_to_complex(1)
        self.blocks_float_to_complex_0_0_1_0 = blocks.float_to_complex(1)
        self.blocks_float_to_complex_0_0 = blocks.float_to_complex(1)
        self.blocks_complex_to_float_0 = blocks.complex_to_float(1)
        self.blocks_add_xx_3 = blocks.add_vff(1)
        self.blocks_add_xx_1_0 = blocks.add_vcc(1)
        self.blocks_add_xx_1 = blocks.add_vcc(1)
        self.blocks_add_xx_0 = blocks.add_vcc(1)
        self.blocks_add_const_vxx_0_0 = blocks.add_const_ff(1)
        self.blocks_add_const_vxx_0 = blocks.add_const_ff(1)
        self.analog_sig_source_x_2_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, variable_fc, 1, 0, 0)
        self.analog_sig_source_x_2 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, variable_fc, 1, 0, 0)
        self.analog_sig_source_x_0_0 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, variable_y_freq, 1, 0, 0)
        self.analog_sig_source_x_0 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, variable_x_freq, 1, 0, 0)
        self.analog_noise_source_x_0 = analog.noise_source_c(analog.GR_GAUSSIAN, 0.01, 0)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_noise_source_x_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_const_vxx_3, 0))
        self.connect((self.analog_sig_source_x_0_0, 0), (self.blocks_multiply_const_vxx_3_0, 0))
        self.connect((self.analog_sig_source_x_2, 0), (self.blocks_multiply_xx_0_0, 1))
        self.connect((self.analog_sig_source_x_2_0, 0), (self.blocks_multiply_xx_0_0_0, 1))
        self.connect((self.blocks_add_const_vxx_0, 0), (self.blocks_float_to_complex_0_0, 0))
        self.connect((self.blocks_add_const_vxx_0_0, 0), (self.blocks_float_to_complex_0_0, 1))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_multiply_xx_0_3, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_multiply_xx_0_3, 1))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_multiply_xx_0_3_0, 1))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_multiply_xx_0_3_0, 2))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_multiply_xx_0_3_0, 0))
        self.connect((self.blocks_add_xx_1, 0), (self.blocks_multiply_xx_0_0_0, 0))
        self.connect((self.blocks_add_xx_1_0, 0), (self.blocks_complex_to_float_0, 0))
        self.connect((self.blocks_add_xx_3, 0), (self.blocks_float_to_complex_1, 0))
        self.connect((self.blocks_add_xx_3, 0), (self.qtgui_freq_sink_x_0_0, 0))
        self.connect((self.blocks_add_xx_3, 0), (self.qtgui_time_sink_x_0_0, 0))
        self.connect((self.blocks_complex_to_float_0, 0), (self.blocks_add_xx_3, 0))
        self.connect((self.blocks_complex_to_float_0, 1), (self.blocks_add_xx_3, 1))
        self.connect((self.blocks_float_to_complex_0_0, 0), (self.blocks_multiply_xx_0_0, 0))
        self.connect((self.blocks_float_to_complex_0_0_1_0, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.blocks_float_to_complex_0_0_1_0, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.blocks_float_to_complex_1, 0), (self.blocks_multiply_const_vxx_1_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_add_xx_1, 0))
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.blocks_add_xx_1_0, 0))
        self.connect((self.blocks_multiply_const_vxx_1, 0), (self.blocks_add_xx_1, 1))
        self.connect((self.blocks_multiply_const_vxx_1_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.blocks_multiply_const_vxx_1_1, 0), (self.blocks_add_xx_1_0, 1))
        self.connect((self.blocks_multiply_const_vxx_2, 0), (self.blocks_add_xx_1, 2))
        self.connect((self.blocks_multiply_const_vxx_2_0, 0), (self.blocks_add_xx_1_0, 2))
        self.connect((self.blocks_multiply_const_vxx_3, 0), (self.blocks_add_const_vxx_0, 0))
        self.connect((self.blocks_multiply_const_vxx_3, 0), (self.blocks_float_to_complex_0_0_1_0, 0))
        self.connect((self.blocks_multiply_const_vxx_3_0, 0), (self.blocks_add_const_vxx_0_0, 0))
        self.connect((self.blocks_multiply_const_vxx_3_0, 0), (self.blocks_float_to_complex_0_0_1_0, 1))
        self.connect((self.blocks_multiply_xx_0_0, 0), (self.blocks_multiply_const_vxx_0_0, 0))
        self.connect((self.blocks_multiply_xx_0_0, 0), (self.blocks_multiply_xx_0_3_0_0, 0))
        self.connect((self.blocks_multiply_xx_0_0, 0), (self.blocks_multiply_xx_0_3_0_0, 1))
        self.connect((self.blocks_multiply_xx_0_0, 0), (self.blocks_multiply_xx_0_3_0_0, 2))
        self.connect((self.blocks_multiply_xx_0_0, 0), (self.blocks_multiply_xx_0_3_1, 0))
        self.connect((self.blocks_multiply_xx_0_0, 0), (self.blocks_multiply_xx_0_3_1, 1))
        self.connect((self.blocks_multiply_xx_0_0_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.blocks_multiply_xx_0_0_0, 0), (self.low_pass_filter_0_0, 0))
        self.connect((self.blocks_multiply_xx_0_3, 0), (self.blocks_multiply_const_vxx_1, 0))
        self.connect((self.blocks_multiply_xx_0_3_0, 0), (self.blocks_multiply_const_vxx_2, 0))
        self.connect((self.blocks_multiply_xx_0_3_0_0, 0), (self.blocks_multiply_const_vxx_2_0, 0))
        self.connect((self.blocks_multiply_xx_0_3_1, 0), (self.blocks_multiply_const_vxx_1_1, 0))
        self.connect((self.blocks_throttle_0, 0), (self.qtgui_freq_sink_x_0, 2))
        self.connect((self.blocks_throttle_0, 0), (self.qtgui_time_sink_x_0, 2))
        self.connect((self.low_pass_filter_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.low_pass_filter_0_0, 0), (self.qtgui_freq_sink_x_0, 1))
        self.connect((self.low_pass_filter_0_0, 0), (self.qtgui_time_sink_x_0, 1))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "Lab0")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_variable_y_freq(self):
        return self.variable_y_freq

    def set_variable_y_freq(self, variable_y_freq):
        self.variable_y_freq = variable_y_freq
        self.analog_sig_source_x_0_0.set_frequency(self.variable_y_freq)

    def get_variable_x_freq(self):
        return self.variable_x_freq

    def set_variable_x_freq(self, variable_x_freq):
        self.variable_x_freq = variable_x_freq
        self.analog_sig_source_x_0.set_frequency(self.variable_x_freq)
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, (2*self.variable_x_freq), self.variable_x_freq, window.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_0.set_taps(firdes.low_pass(1, self.samp_rate, (2*self.variable_x_freq), self.variable_x_freq, window.WIN_HAMMING, 6.76))

    def get_variable_m(self):
        return self.variable_m

    def set_variable_m(self, variable_m):
        self.variable_m = variable_m
        self.blocks_multiply_const_vxx_3.set_k(self.variable_m)
        self.blocks_multiply_const_vxx_3_0.set_k(self.variable_m)

    def get_variable_fc(self):
        return self.variable_fc

    def set_variable_fc(self, variable_fc):
        self.variable_fc = variable_fc
        self.analog_sig_source_x_2.set_frequency(self.variable_fc)
        self.analog_sig_source_x_2_0.set_frequency(self.variable_fc)

    def get_variable_channel_atenuation(self):
        return self.variable_channel_atenuation

    def set_variable_channel_atenuation(self, variable_channel_atenuation):
        self.variable_channel_atenuation = variable_channel_atenuation
        self.blocks_multiply_const_vxx_1_0.set_k(self.variable_channel_atenuation)

    def get_variable_a3(self):
        return self.variable_a3

    def set_variable_a3(self, variable_a3):
        self.variable_a3 = variable_a3
        self.blocks_multiply_const_vxx_2.set_k(self.variable_a3)
        self.blocks_multiply_const_vxx_2_0.set_k(self.variable_a3)

    def get_variable_a2(self):
        return self.variable_a2

    def set_variable_a2(self, variable_a2):
        self.variable_a2 = variable_a2
        self.blocks_multiply_const_vxx_1.set_k(self.variable_a2)
        self.blocks_multiply_const_vxx_1_1.set_k(self.variable_a2)

    def get_variable_a1(self):
        return self.variable_a1

    def set_variable_a1(self, variable_a1):
        self.variable_a1 = variable_a1
        self.blocks_multiply_const_vxx_0.set_k(self.variable_a1)
        self.blocks_multiply_const_vxx_0_0.set_k(self.variable_a1)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_2.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_2_0.set_sampling_freq(self.samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, (2*self.variable_x_freq), self.variable_x_freq, window.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_0.set_taps(firdes.low_pass(1, self.samp_rate, (2*self.variable_x_freq), self.variable_x_freq, window.WIN_HAMMING, 6.76))
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_freq_sink_x_0_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_0_0.set_samp_rate(self.samp_rate)




def main(top_block_cls=Lab0, options=None):

    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
