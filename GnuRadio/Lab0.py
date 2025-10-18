#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Not titled yet
# GNU Radio version: 3.10.12.0

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
import threading



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

        self.settings = Qt.QSettings("gnuradio/flowgraphs", "Lab0")

        try:
            geometry = self.settings.value("geometry")
            if geometry:
                self.restoreGeometry(geometry)
        except BaseException as exc:
            print(f"Qt GUI: Could not restore geometry: {str(exc)}", file=sys.stderr)
        self.flowgraph_started = threading.Event()

        ##################################################
        # Variables
        ##################################################
        self.variable_y_freq = variable_y_freq = 250
        self.variable_x_freq = variable_x_freq = 500
        self.variable_m = variable_m = 1
        self.variable_channel_atenuation = variable_channel_atenuation = 4
        self.samp_rate = samp_rate = 768000
        self.receiver_power_amplifier_a3 = receiver_power_amplifier_a3 = 0
        self.receiver_power_amplifier_a2 = receiver_power_amplifier_a2 = 0
        self.receiver_power_amplifier_a1 = receiver_power_amplifier_a1 = 1
        self.modulation_frequency = modulation_frequency = 100000
        self.emitter_transition_LP = emitter_transition_LP = 500
        self.emitter_power_amplifier_a3 = emitter_power_amplifier_a3 = 0
        self.emitter_power_amplifier_a2 = emitter_power_amplifier_a2 = 0
        self.emitter_power_amplifier_a1 = emitter_power_amplifier_a1 = 1
        self.emitter_cutoff_LP = emitter_cutoff_LP = 40000
        self.bandpass_bandwidth = bandpass_bandwidth = 90000

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
        self._variable_channel_atenuation_range = qtgui.Range(1, 100, 1, 4, 200)
        self._variable_channel_atenuation_win = qtgui.RangeWidget(self._variable_channel_atenuation_range, self.set_variable_channel_atenuation, "atenuation", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._variable_channel_atenuation_win)
        self._receiver_power_amplifier_a3_range = qtgui.Range(-5, 5, 0.1, 0, 200)
        self._receiver_power_amplifier_a3_win = qtgui.RangeWidget(self._receiver_power_amplifier_a3_range, self.set_receiver_power_amplifier_a3, "a3", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._receiver_power_amplifier_a3_win)
        self._receiver_power_amplifier_a2_range = qtgui.Range(-10, 10, 1, 0, 200)
        self._receiver_power_amplifier_a2_win = qtgui.RangeWidget(self._receiver_power_amplifier_a2_range, self.set_receiver_power_amplifier_a2, "a2", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._receiver_power_amplifier_a2_win)
        self._receiver_power_amplifier_a1_range = qtgui.Range(0, 20, 0.5, 1, 200)
        self._receiver_power_amplifier_a1_win = qtgui.RangeWidget(self._receiver_power_amplifier_a1_range, self.set_receiver_power_amplifier_a1, "a1", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._receiver_power_amplifier_a1_win)
        self._modulation_frequency_range = qtgui.Range(10000, 200000, 10000, 100000, 200)
        self._modulation_frequency_win = qtgui.RangeWidget(self._modulation_frequency_range, self.set_modulation_frequency, "modulation frequency", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._modulation_frequency_win)
        self._emitter_transition_LP_range = qtgui.Range(0, 1000, 10, 500, 200)
        self._emitter_transition_LP_win = qtgui.RangeWidget(self._emitter_transition_LP_range, self.set_emitter_transition_LP, "Emitter transition freq", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._emitter_transition_LP_win)
        self._emitter_power_amplifier_a3_range = qtgui.Range(-5, 5, 0.1, 0, 200)
        self._emitter_power_amplifier_a3_win = qtgui.RangeWidget(self._emitter_power_amplifier_a3_range, self.set_emitter_power_amplifier_a3, "Emitter amplifier a3", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._emitter_power_amplifier_a3_win)
        self._emitter_power_amplifier_a1_range = qtgui.Range(0, 20, 0.5, 1, 200)
        self._emitter_power_amplifier_a1_win = qtgui.RangeWidget(self._emitter_power_amplifier_a1_range, self.set_emitter_power_amplifier_a1, "Emitter amplifier a1", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._emitter_power_amplifier_a1_win)
        self._emitter_cutoff_LP_range = qtgui.Range(100, 45000, 10, 40000, 200)
        self._emitter_cutoff_LP_win = qtgui.RangeWidget(self._emitter_cutoff_LP_range, self.set_emitter_cutoff_LP, "Emitter cutoff freq", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._emitter_cutoff_LP_win)
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
        self.qtgui_time_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_AUTO, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_0.enable_autoscale(True)
        self.qtgui_time_sink_x_0_0.enable_grid(False)
        self.qtgui_time_sink_x_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0_0.enable_stem_plot(False)


        labels = ['emitter_output', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
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
        self.qtgui_freq_sink_x_1 = qtgui.freq_sink_f(
            1024, #size
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            "", #name
            1,
            None # parent
        )
        self.qtgui_freq_sink_x_1.set_update_time(0.10)
        self.qtgui_freq_sink_x_1.set_y_axis((-140), 10)
        self.qtgui_freq_sink_x_1.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_1.enable_autoscale(False)
        self.qtgui_freq_sink_x_1.enable_grid(False)
        self.qtgui_freq_sink_x_1.set_fft_average(1.0)
        self.qtgui_freq_sink_x_1.enable_axis_labels(True)
        self.qtgui_freq_sink_x_1.enable_control_panel(False)
        self.qtgui_freq_sink_x_1.set_fft_window_normalized(False)


        self.qtgui_freq_sink_x_1.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_1.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_1.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_1.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_1.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_1_win = sip.wrapinstance(self.qtgui_freq_sink_x_1.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_1_win)
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

        labels = ['Emitter_output', 'original_sine_signal', 'processed_cosine_signal', 'processed_sine_signal', '',
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
        self.low_pass_filter_1_0 = filter.fir_filter_fff(
            1,
            firdes.low_pass(
                1,
                samp_rate,
                emitter_cutoff_LP,
                emitter_transition_LP,
                window.WIN_HAMMING,
                6.76))
        self.low_pass_filter_1 = filter.fir_filter_fff(
            1,
            firdes.low_pass(
                1,
                samp_rate,
                emitter_cutoff_LP,
                emitter_transition_LP,
                window.WIN_HAMMING,
                6.76))
        self.low_pass_filter_0_0 = filter.fir_filter_fff(
            1,
            firdes.low_pass(
                1,
                samp_rate,
                emitter_cutoff_LP,
                emitter_transition_LP,
                window.WIN_HAMMING,
                6.76))
        self.low_pass_filter_0 = filter.fir_filter_fff(
            1,
            firdes.low_pass(
                1,
                samp_rate,
                emitter_cutoff_LP,
                emitter_transition_LP,
                window.WIN_HAMMING,
                6.76))
        self._emitter_power_amplifier_a2_range = qtgui.Range(-10, 10, 1, 0, 200)
        self._emitter_power_amplifier_a2_win = qtgui.RangeWidget(self._emitter_power_amplifier_a2_range, self.set_emitter_power_amplifier_a2, "Emitter amplier a2", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._emitter_power_amplifier_a2_win)
        self.blocks_null_source_0 = blocks.null_source(gr.sizeof_float*1)
        self.blocks_null_sink_0 = blocks.null_sink(gr.sizeof_float*1)
        self.blocks_multiply_xx_0_3_1 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0_3_0_0 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0_3_0 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0_3 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0_1 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0_0_0 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0_0 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0 = blocks.multiply_vff(1)
        self.blocks_multiply_const_vxx_3_0 = blocks.multiply_const_ff(variable_m)
        self.blocks_multiply_const_vxx_3 = blocks.multiply_const_ff(variable_m)
        self.blocks_multiply_const_vxx_2_0 = blocks.multiply_const_ff(emitter_power_amplifier_a3)
        self.blocks_multiply_const_vxx_2 = blocks.multiply_const_ff(receiver_power_amplifier_a3)
        self.blocks_multiply_const_vxx_1_1 = blocks.multiply_const_ff(emitter_power_amplifier_a3)
        self.blocks_multiply_const_vxx_1_0 = blocks.multiply_const_ff((1/variable_channel_atenuation))
        self.blocks_multiply_const_vxx_1 = blocks.multiply_const_ff(receiver_power_amplifier_a2)
        self.blocks_multiply_const_vxx_0_0 = blocks.multiply_const_ff(emitter_power_amplifier_a1)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_ff(receiver_power_amplifier_a1)
        self.blocks_add_xx_3 = blocks.add_vff(1)
        self.blocks_add_xx_1_0 = blocks.add_vff(1)
        self.blocks_add_xx_1 = blocks.add_vff(1)
        self.blocks_add_xx_0 = blocks.add_vff(1)
        self._bandpass_bandwidth_range = qtgui.Range(1, 100000, 1000, 90000, 200)
        self._bandpass_bandwidth_win = qtgui.RangeWidget(self._bandpass_bandwidth_range, self.set_bandpass_bandwidth, "Signal frequency", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._bandpass_bandwidth_win)
        self.analog_sig_source_x_0_0_1 = analog.sig_source_f(samp_rate, analog.GR_SIN_WAVE, modulation_frequency, 1, 0, 0)
        self.analog_sig_source_x_0_0_0 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, modulation_frequency, 1, 0, 0)
        self.analog_sig_source_x_0_0 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, variable_y_freq, 1, 0, 0)
        self.analog_sig_source_x_0 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, variable_x_freq, 1, 0, 0)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0, 0), (self.low_pass_filter_1, 0))
        self.connect((self.analog_sig_source_x_0_0, 0), (self.low_pass_filter_1_0, 0))
        self.connect((self.analog_sig_source_x_0_0_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.analog_sig_source_x_0_0_0, 0), (self.blocks_multiply_xx_0_1, 0))
        self.connect((self.analog_sig_source_x_0_0_1, 0), (self.blocks_multiply_xx_0_0, 0))
        self.connect((self.analog_sig_source_x_0_0_1, 0), (self.blocks_multiply_xx_0_0_0, 1))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_multiply_const_vxx_1_0, 0))
        self.connect((self.blocks_add_xx_1, 0), (self.blocks_multiply_xx_0_0_0, 0))
        self.connect((self.blocks_add_xx_1, 0), (self.blocks_multiply_xx_0_1, 1))
        self.connect((self.blocks_add_xx_1_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.blocks_add_xx_1_0, 0), (self.qtgui_freq_sink_x_0_0, 0))
        self.connect((self.blocks_add_xx_1_0, 0), (self.qtgui_freq_sink_x_1, 0))
        self.connect((self.blocks_add_xx_1_0, 0), (self.qtgui_time_sink_x_0_0, 0))
        self.connect((self.blocks_add_xx_3, 0), (self.blocks_multiply_const_vxx_0_0, 0))
        self.connect((self.blocks_add_xx_3, 0), (self.blocks_multiply_xx_0_3_0_0, 2))
        self.connect((self.blocks_add_xx_3, 0), (self.blocks_multiply_xx_0_3_0_0, 1))
        self.connect((self.blocks_add_xx_3, 0), (self.blocks_multiply_xx_0_3_0_0, 0))
        self.connect((self.blocks_add_xx_3, 0), (self.blocks_multiply_xx_0_3_1, 1))
        self.connect((self.blocks_add_xx_3, 0), (self.blocks_multiply_xx_0_3_1, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_add_xx_1, 0))
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.blocks_add_xx_1_0, 0))
        self.connect((self.blocks_multiply_const_vxx_1, 0), (self.blocks_add_xx_1, 1))
        self.connect((self.blocks_multiply_const_vxx_1_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_multiply_const_vxx_1_0, 0), (self.blocks_multiply_xx_0_3, 0))
        self.connect((self.blocks_multiply_const_vxx_1_0, 0), (self.blocks_multiply_xx_0_3, 1))
        self.connect((self.blocks_multiply_const_vxx_1_0, 0), (self.blocks_multiply_xx_0_3_0, 1))
        self.connect((self.blocks_multiply_const_vxx_1_0, 0), (self.blocks_multiply_xx_0_3_0, 2))
        self.connect((self.blocks_multiply_const_vxx_1_0, 0), (self.blocks_multiply_xx_0_3_0, 0))
        self.connect((self.blocks_multiply_const_vxx_1_1, 0), (self.blocks_add_xx_1_0, 1))
        self.connect((self.blocks_multiply_const_vxx_2, 0), (self.blocks_add_xx_1, 2))
        self.connect((self.blocks_multiply_const_vxx_2_0, 0), (self.blocks_add_xx_1_0, 2))
        self.connect((self.blocks_multiply_const_vxx_3, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.blocks_multiply_const_vxx_3, 0), (self.blocks_null_sink_0, 0))
        self.connect((self.blocks_multiply_const_vxx_3_0, 0), (self.blocks_multiply_xx_0_0, 1))
        self.connect((self.blocks_multiply_const_vxx_3_0, 0), (self.blocks_null_sink_0, 1))
        self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_add_xx_3, 0))
        self.connect((self.blocks_multiply_xx_0_0, 0), (self.blocks_add_xx_3, 1))
        self.connect((self.blocks_multiply_xx_0_0_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.blocks_multiply_xx_0_1, 0), (self.low_pass_filter_0_0, 0))
        self.connect((self.blocks_multiply_xx_0_3, 0), (self.blocks_multiply_const_vxx_1, 0))
        self.connect((self.blocks_multiply_xx_0_3_0, 0), (self.blocks_multiply_const_vxx_2, 0))
        self.connect((self.blocks_multiply_xx_0_3_0_0, 0), (self.blocks_multiply_const_vxx_2_0, 0))
        self.connect((self.blocks_multiply_xx_0_3_1, 0), (self.blocks_multiply_const_vxx_1_1, 0))
        self.connect((self.blocks_null_source_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.low_pass_filter_0, 0), (self.blocks_null_sink_0, 3))
        self.connect((self.low_pass_filter_0_0, 0), (self.blocks_null_sink_0, 2))
        self.connect((self.low_pass_filter_1, 0), (self.blocks_multiply_const_vxx_3, 0))
        self.connect((self.low_pass_filter_1_0, 0), (self.blocks_multiply_const_vxx_3_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("gnuradio/flowgraphs", "Lab0")
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

    def get_variable_m(self):
        return self.variable_m

    def set_variable_m(self, variable_m):
        self.variable_m = variable_m
        self.blocks_multiply_const_vxx_3.set_k(self.variable_m)
        self.blocks_multiply_const_vxx_3_0.set_k(self.variable_m)

    def get_variable_channel_atenuation(self):
        return self.variable_channel_atenuation

    def set_variable_channel_atenuation(self, variable_channel_atenuation):
        self.variable_channel_atenuation = variable_channel_atenuation
        self.blocks_multiply_const_vxx_1_0.set_k((1/self.variable_channel_atenuation))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_0_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_0_1.set_sampling_freq(self.samp_rate)
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, self.emitter_cutoff_LP, self.emitter_transition_LP, window.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_0.set_taps(firdes.low_pass(1, self.samp_rate, self.emitter_cutoff_LP, self.emitter_transition_LP, window.WIN_HAMMING, 6.76))
        self.low_pass_filter_1.set_taps(firdes.low_pass(1, self.samp_rate, self.emitter_cutoff_LP, self.emitter_transition_LP, window.WIN_HAMMING, 6.76))
        self.low_pass_filter_1_0.set_taps(firdes.low_pass(1, self.samp_rate, self.emitter_cutoff_LP, self.emitter_transition_LP, window.WIN_HAMMING, 6.76))
        self.qtgui_freq_sink_x_0_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_time_sink_x_0_0.set_samp_rate(self.samp_rate)
        self.qtgui_freq_sink_x_1.set_frequency_range(0, self.samp_rate)

    def get_receiver_power_amplifier_a3(self):
        return self.receiver_power_amplifier_a3

    def set_receiver_power_amplifier_a3(self, receiver_power_amplifier_a3):
        self.receiver_power_amplifier_a3 = receiver_power_amplifier_a3
        self.blocks_multiply_const_vxx_2.set_k(self.receiver_power_amplifier_a3)

    def get_receiver_power_amplifier_a2(self):
        return self.receiver_power_amplifier_a2

    def set_receiver_power_amplifier_a2(self, receiver_power_amplifier_a2):
        self.receiver_power_amplifier_a2 = receiver_power_amplifier_a2
        self.blocks_multiply_const_vxx_1.set_k(self.receiver_power_amplifier_a2)

    def get_receiver_power_amplifier_a1(self):
        return self.receiver_power_amplifier_a1

    def set_receiver_power_amplifier_a1(self, receiver_power_amplifier_a1):
        self.receiver_power_amplifier_a1 = receiver_power_amplifier_a1
        self.blocks_multiply_const_vxx_0.set_k(self.receiver_power_amplifier_a1)

    def get_modulation_frequency(self):
        return self.modulation_frequency

    def set_modulation_frequency(self, modulation_frequency):
        self.modulation_frequency = modulation_frequency
        self.analog_sig_source_x_0_0_0.set_frequency(self.modulation_frequency)
        self.analog_sig_source_x_0_0_1.set_frequency(self.modulation_frequency)

    def get_emitter_transition_LP(self):
        return self.emitter_transition_LP

    def set_emitter_transition_LP(self, emitter_transition_LP):
        self.emitter_transition_LP = emitter_transition_LP
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, self.emitter_cutoff_LP, self.emitter_transition_LP, window.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_0.set_taps(firdes.low_pass(1, self.samp_rate, self.emitter_cutoff_LP, self.emitter_transition_LP, window.WIN_HAMMING, 6.76))
        self.low_pass_filter_1.set_taps(firdes.low_pass(1, self.samp_rate, self.emitter_cutoff_LP, self.emitter_transition_LP, window.WIN_HAMMING, 6.76))
        self.low_pass_filter_1_0.set_taps(firdes.low_pass(1, self.samp_rate, self.emitter_cutoff_LP, self.emitter_transition_LP, window.WIN_HAMMING, 6.76))

    def get_emitter_power_amplifier_a3(self):
        return self.emitter_power_amplifier_a3

    def set_emitter_power_amplifier_a3(self, emitter_power_amplifier_a3):
        self.emitter_power_amplifier_a3 = emitter_power_amplifier_a3
        self.blocks_multiply_const_vxx_1_1.set_k(self.emitter_power_amplifier_a3)
        self.blocks_multiply_const_vxx_2_0.set_k(self.emitter_power_amplifier_a3)

    def get_emitter_power_amplifier_a2(self):
        return self.emitter_power_amplifier_a2

    def set_emitter_power_amplifier_a2(self, emitter_power_amplifier_a2):
        self.emitter_power_amplifier_a2 = emitter_power_amplifier_a2

    def get_emitter_power_amplifier_a1(self):
        return self.emitter_power_amplifier_a1

    def set_emitter_power_amplifier_a1(self, emitter_power_amplifier_a1):
        self.emitter_power_amplifier_a1 = emitter_power_amplifier_a1
        self.blocks_multiply_const_vxx_0_0.set_k(self.emitter_power_amplifier_a1)

    def get_emitter_cutoff_LP(self):
        return self.emitter_cutoff_LP

    def set_emitter_cutoff_LP(self, emitter_cutoff_LP):
        self.emitter_cutoff_LP = emitter_cutoff_LP
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, self.emitter_cutoff_LP, self.emitter_transition_LP, window.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_0.set_taps(firdes.low_pass(1, self.samp_rate, self.emitter_cutoff_LP, self.emitter_transition_LP, window.WIN_HAMMING, 6.76))
        self.low_pass_filter_1.set_taps(firdes.low_pass(1, self.samp_rate, self.emitter_cutoff_LP, self.emitter_transition_LP, window.WIN_HAMMING, 6.76))
        self.low_pass_filter_1_0.set_taps(firdes.low_pass(1, self.samp_rate, self.emitter_cutoff_LP, self.emitter_transition_LP, window.WIN_HAMMING, 6.76))

    def get_bandpass_bandwidth(self):
        return self.bandpass_bandwidth

    def set_bandpass_bandwidth(self, bandpass_bandwidth):
        self.bandpass_bandwidth = bandpass_bandwidth




def main(top_block_cls=Lab0, options=None):

    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()
    tb.flowgraph_started.set()

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
