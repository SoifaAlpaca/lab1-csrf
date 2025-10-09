#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: WAV to AM to Audio
# GNU Radio version: 3.10.12.0

from PyQt5 import Qt
from gnuradio import qtgui
from PyQt5 import QtCore
from gnuradio import analog
from gnuradio import audio
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



class Wav_AM(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "WAV to AM to Audio", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("WAV to AM to Audio")
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

        self.settings = Qt.QSettings("gnuradio/flowgraphs", "Wav_AM")

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
        self.variable_x_freq = variable_x_freq = 500
        self.variable_m = variable_m = 1
        self.variable_fc = variable_fc = 100000
        self.variable_channel_atenuation = variable_channel_atenuation = 1
        self.variable_a3 = variable_a3 = 0
        self.variable_a2 = variable_a2 = 0
        self.variable_a1 = variable_a1 = 7
        self.variable_Base_Band = variable_Base_Band = 40000
        self.samp_rate = samp_rate = 768000

        ##################################################
        # Blocks
        ##################################################

        self._variable_m_range = qtgui.Range(0, 1000, 1, 1, 200)
        self._variable_m_win = qtgui.RangeWidget(self._variable_m_range, self.set_variable_m, "modulation index", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._variable_m_win)
        self._variable_fc_range = qtgui.Range(0, 100000, 1, 100000, 200)
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
        self._variable_x_freq_range = qtgui.Range(0, 5000, 1, 500, 200)
        self._variable_x_freq_win = qtgui.RangeWidget(self._variable_x_freq_range, self.set_variable_x_freq, "Signal frequency", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._variable_x_freq_win)
        self._variable_Base_Band_range = qtgui.Range(1000, 100000, 1, 40000, 200)
        self._variable_Base_Band_win = qtgui.RangeWidget(self._variable_Base_Band_range, self.set_variable_Base_Band, "Base Band, Band", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._variable_Base_Band_win)
        self.rational_resampler_xxx_0 = filter.rational_resampler_fff(
                interpolation=16,
                decimation=1,
                taps=[],
                fractional_bw=0)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_f(
            1024, #size
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            "", #name
            2,
            None # parent
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis((-140), 10)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(False)
        self.qtgui_freq_sink_x_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)
        self.qtgui_freq_sink_x_0.set_fft_window_normalized(False)


        self.qtgui_freq_sink_x_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(2):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_0_win)
        self.low_pass_filter_0_0 = filter.interp_fir_filter_fff(
            1,
            firdes.low_pass(
                1,
                samp_rate,
                30000,
                500,
                window.WIN_BLACKMAN,
                6.76))
        self.low_pass_filter_0 = filter.interp_fir_filter_fff(
            1,
            firdes.low_pass(
                1,
                samp_rate,
                30000,
                500,
                window.WIN_BLACKMAN,
                6.76))
        self.blocks_wavfile_source_0 = blocks.wavfile_source('/Users/martim/Downloads/output.wav', True)
        self.blocks_null_sink_0 = blocks.null_sink(gr.sizeof_float*1)
        self.blocks_multiply_xx_1 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0_3_0 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0_3 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0 = blocks.multiply_vff(1)
        self.blocks_multiply_const_vxx_3 = blocks.multiply_const_ff(variable_m)
        self.blocks_multiply_const_vxx_2 = blocks.multiply_const_ff(variable_a3)
        self.blocks_multiply_const_vxx_1_0 = blocks.multiply_const_ff(variable_channel_atenuation)
        self.blocks_multiply_const_vxx_1 = blocks.multiply_const_ff(variable_a2)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_ff(variable_a1)
        self.blocks_add_xx_1 = blocks.add_vff(1)
        self.blocks_add_xx_0 = blocks.add_vff(1)
        self.blocks_add_const_vxx_0 = blocks.add_const_ff(0)
        self.audio_sink_0 = audio.sink(samp_rate, '', True)
        self.analog_sig_source_x_2_0 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, variable_fc, 1, 0, 0)
        self.analog_sig_source_x_0_0 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, variable_fc, 1, 0, 0)
        self.analog_const_source_x_0 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, 0)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_const_source_x_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.analog_sig_source_x_0_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.analog_sig_source_x_2_0, 0), (self.blocks_multiply_xx_1, 1))
        self.connect((self.blocks_add_const_vxx_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_multiply_const_vxx_1_0, 0))
        self.connect((self.blocks_add_xx_1, 0), (self.blocks_multiply_xx_1, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_add_xx_1, 0))
        self.connect((self.blocks_multiply_const_vxx_1, 0), (self.blocks_add_xx_1, 1))
        self.connect((self.blocks_multiply_const_vxx_1_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_multiply_const_vxx_1_0, 0), (self.blocks_multiply_xx_0_3, 1))
        self.connect((self.blocks_multiply_const_vxx_1_0, 0), (self.blocks_multiply_xx_0_3, 0))
        self.connect((self.blocks_multiply_const_vxx_1_0, 0), (self.blocks_multiply_xx_0_3_0, 2))
        self.connect((self.blocks_multiply_const_vxx_1_0, 0), (self.blocks_multiply_xx_0_3_0, 0))
        self.connect((self.blocks_multiply_const_vxx_1_0, 0), (self.blocks_multiply_xx_0_3_0, 1))
        self.connect((self.blocks_multiply_const_vxx_2, 0), (self.blocks_add_xx_1, 2))
        self.connect((self.blocks_multiply_const_vxx_3, 0), (self.blocks_add_const_vxx_0, 0))
        self.connect((self.blocks_multiply_const_vxx_3, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.blocks_multiply_xx_0_3, 0), (self.blocks_multiply_const_vxx_1, 0))
        self.connect((self.blocks_multiply_xx_0_3_0, 0), (self.blocks_multiply_const_vxx_2, 0))
        self.connect((self.blocks_multiply_xx_1, 0), (self.low_pass_filter_0, 0))
        self.connect((self.blocks_wavfile_source_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.audio_sink_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.blocks_null_sink_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.qtgui_freq_sink_x_0, 1))
        self.connect((self.low_pass_filter_0_0, 0), (self.blocks_multiply_const_vxx_3, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.low_pass_filter_0_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("gnuradio/flowgraphs", "Wav_AM")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_variable_x_freq(self):
        return self.variable_x_freq

    def set_variable_x_freq(self, variable_x_freq):
        self.variable_x_freq = variable_x_freq

    def get_variable_m(self):
        return self.variable_m

    def set_variable_m(self, variable_m):
        self.variable_m = variable_m
        self.blocks_multiply_const_vxx_3.set_k(self.variable_m)

    def get_variable_fc(self):
        return self.variable_fc

    def set_variable_fc(self, variable_fc):
        self.variable_fc = variable_fc
        self.analog_sig_source_x_0_0.set_frequency(self.variable_fc)
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

    def get_variable_a2(self):
        return self.variable_a2

    def set_variable_a2(self, variable_a2):
        self.variable_a2 = variable_a2
        self.blocks_multiply_const_vxx_1.set_k(self.variable_a2)

    def get_variable_a1(self):
        return self.variable_a1

    def set_variable_a1(self, variable_a1):
        self.variable_a1 = variable_a1
        self.blocks_multiply_const_vxx_0.set_k(self.variable_a1)

    def get_variable_Base_Band(self):
        return self.variable_Base_Band

    def set_variable_Base_Band(self, variable_Base_Band):
        self.variable_Base_Band = variable_Base_Band

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.analog_sig_source_x_0_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_2_0.set_sampling_freq(self.samp_rate)
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, 30000, 500, window.WIN_BLACKMAN, 6.76))
        self.low_pass_filter_0_0.set_taps(firdes.low_pass(1, self.samp_rate, 30000, 500, window.WIN_BLACKMAN, 6.76))
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate)




def main(top_block_cls=Wav_AM, options=None):

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
