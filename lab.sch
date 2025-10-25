<Qucs Schematic 25.2.0>
<Properties>
  <View=459,245,1279,807,1.41219,0,0>
  <Grid=10,10,1>
  <DataSet=lab.dat>
  <DataDisplay=lab.dpl>
  <OpenDisplay=0>
  <Script=lab.m>
  <RunScript=0>
  <showFrame=0>
  <FrameText0=Title>
  <FrameText1=Drawn By:>
  <FrameText2=Date:>
  <FrameText3=Revision:>
</Properties>
<Symbol>
</Symbol>
<Components>
  <R R1 1 1040 620 15 -26 0 1 "200 Ohm" 1 "26.85" 0 "0.0" 0 "0.0" 0 "26.85" 0 "european" 0>
  <GND * 1 1040 670 0 0 0 0>
  <GND * 1 810 720 0 0 0 0>
  <NutmegEq Zin 1 500 600 -21 14 0 0 "ALL" 1 "Zin=V(in) / I(V1)" 1>
  <GND * 1 930 710 0 0 0 0>
  <Vac V1 1 810 660 18 -26 0 1 "1 V" 1 "1" 1 "0" 0 "0" 0 "0" 0 "0" 0>
  <.AC AC1 1 470 270 0 31 0 0 "lin" 1 "100kHz" 1 "700kHz" 1 "200" 1 "no" 0>
  <L L5 1 880 590 -26 10 0 0 "28.129uH" 1 "" 0>
  <C C5 1 930 660 15 -20 0 1 "2.813nF" 1 "" 0 "neutral" 0>
</Components>
<Wires>
  <1040 650 1040 670 "" 0 0 0 "">
  <810 590 810 630 "in" 756 593 8 "">
  <810 690 810 720 "" 0 0 0 "">
  <930 590 930 630 "" 0 0 0 "">
  <930 590 910 590 "" 0 0 0 "">
  <810 590 850 590 "" 0 0 0 "">
  <930 590 1040 590 "" 0 0 0 "">
  <930 690 930 710 "" 0 0 0 "">
</Wires>
<Diagrams>
  <Rect 840 430 240 160 3 #c0c0c0 1 00 1 0 0.2 1 1 -0.1 0.5 1.1 1 -0.1 0.5 1.1 315 0 225 1 0 0 "" "" "">
	<"ngspice/ac.zin" #0000ff 1 3 0 0 0>
  </Rect>
</Diagrams>
<Paintings>
  <Text 800 550 12 #000000 0 "Port 1">
  <Text 950 560 12 #000000 0 "Port 2">
  <Text 580 770 12 #000000 0 "Port 1">
  <Text 770 770 12 #000000 0 "Port 2">
</Paintings>
