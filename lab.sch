<Qucs Schematic 25.2.0>
<Properties>
  <View=466,231,1314,789,1.46416,0,0>
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
  <C C4 1 930 680 15 -20 0 1 "2.2nF" 1 "" 0 "neutral" 0>
  <L L4 1 980 590 -26 10 0 0 "33mH" 1 "" 0>
  <.AC AC1 1 470 270 0 31 0 0 "lin" 1 "1 Hz" 1 "1kHz" 1 "200" 1 "no" 0>
  <Vac V1 1 810 660 18 -26 0 1 "1 V" 1 "100" 1 "0" 0 "0" 0 "0" 0 "0" 0>
</Components>
<Wires>
  <1040 650 1040 670 "" 0 0 0 "">
  <810 590 810 630 "in" 756 593 8 "">
  <810 690 810 720 "" 0 0 0 "">
  <930 590 930 650 "" 0 0 0 "">
  <930 590 950 590 "" 0 0 0 "">
  <810 590 930 590 "" 0 0 0 "">
  <1010 590 1040 590 "" 0 0 0 "">
</Wires>
<Diagrams>
  <Rect 910 490 240 160 3 #c0c0c0 1 00 0 300000 50000 600000 0 0 50 100 1 -1 1 1 315 0 225 1 0 0 "" "" "">
	<"ngspice/ac.zin" #0000ff 1 3 0 0 0>
  </Rect>
</Diagrams>
<Paintings>
  <Text 800 550 12 #000000 0 "Port 1">
  <Text 950 560 12 #000000 0 "Port 2">
</Paintings>
