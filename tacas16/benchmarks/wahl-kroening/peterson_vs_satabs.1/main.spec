vars
s0 s1 s2 s3 s4 s5 s6 s7 s8 s9 s10 s11 s12 s13 s14 s15 s16 l0 l1 l2 l3 l4 l5 l6 l7 l8 l9 l10 l11 l12 l13 

rules
l0>=1, s0>=1 -> 
	l0'=l0-1,
	l1'=l1+1;

l0>=1, s0>=1 -> 
	s0'=s0-1,
	s2'=s2+1,
	l0'=l0-1,
	l1'=l1+1;

l1>=1, s0>=1 -> 
	l1'=l1-1,
	l2'=l2+1;

l1>=1, s0>=1 -> 
	s0'=s0-1,
	s1'=s1+1,
	l1'=l1-1,
	l2'=l2+1;

l2>=1, s0>=1 -> 
	s0'=s0-1,
	s2'=s2+1,
	l2'=l2-1,
	l3'=l3+1;

l4>=1, s0>=1 -> 
;

l4>=1, s0>=1 -> 
	l4'=l4-1,
	l5'=l5+1;

l5>=1, s0>=1 -> 
	s0'=s0-1,
	s2'=s2+1,
	l5'=l5-1,
	l6'=l6+1;

l6>=1, s0>=1 -> 
	s0'=s0-1,
	s16'=s16+1,
	l6'=l6-1,
	l13'=l13+1;

l8>=1, s0>=1 -> 
	l8'=l8-1,
	l9'=l9+1;

l9>=1, s0>=1 -> 
;

l9>=1, s0>=1 -> 
	l9'=l9-1,
	l10'=l10+1;

l10>=1, s0>=1 -> 
	s0'=s0-1,
	s1'=s1+1,
	l10'=l10-1,
	l11'=l11+1;

l11>=1, s0>=1 -> 
	s0'=s0-1,
	s16'=s16+1,
	l11'=l11-1,
	l13'=l13+1;

l0>=1, s1>=1 -> 
	l0'=l0-1,
	l1'=l1+1;

l0>=1, s1>=1 -> 
	s1'=s1-1,
	s3'=s3+1,
	l0'=l0-1,
	l1'=l1+1;

l1>=1, s1>=1 -> 
	s1'=s1-1,
	s0'=s0+1,
	l1'=l1-1,
	l2'=l2+1;

l1>=1, s1>=1 -> 
	l1'=l1-1,
	l2'=l2+1;

l2>=1, s1>=1 -> 
	s1'=s1-1,
	s2'=s2+1,
	l2'=l2-1,
	l3'=l3+1;

l4>=1, s1>=1 -> 
;

l4>=1, s1>=1 -> 
	l4'=l4-1,
	l5'=l5+1;

l5>=1, s1>=1 -> 
	s1'=s1-1,
	s2'=s2+1,
	l5'=l5-1,
	l6'=l6+1;

l6>=1, s1>=1 -> 
	s1'=s1-1,
	s16'=s16+1,
	l6'=l6-1,
	l13'=l13+1;

l8>=1, s1>=1 -> 
	l8'=l8-1,
	l9'=l9+1;

l9>=1, s1>=1 -> 
;

l9>=1, s1>=1 -> 
	l9'=l9-1,
	l10'=l10+1;

l10>=1, s1>=1 -> 
	l10'=l10-1,
	l11'=l11+1;

l11>=1, s1>=1 -> 
	l11'=l11-1,
	l12'=l12+1;

l0>=1, s2>=1 -> 
	s2'=s2-1,
	s0'=s0+1,
	l0'=l0-1,
	l1'=l1+1;

l0>=1, s2>=1 -> 
	l0'=l0-1,
	l1'=l1+1;

l1>=1, s2>=1 -> 
	l1'=l1-1,
	l2'=l2+1;

l1>=1, s2>=1 -> 
	s2'=s2-1,
	s3'=s3+1,
	l1'=l1-1,
	l2'=l2+1;

l2>=1, s2>=1 -> 
	l2'=l2-1,
	l3'=l3+1;

l4>=1, s2>=1 -> 
;

l4>=1, s2>=1 -> 
	l4'=l4-1,
	l5'=l5+1;

l5>=1, s2>=1 -> 
	l5'=l5-1,
	l6'=l6+1;

l6>=1, s2>=1 -> 
	l6'=l6-1,
	l7'=l7+1;

l8>=1, s2>=1 -> 
	l8'=l8-1,
	l9'=l9+1;

l9>=1, s2>=1 -> 
;

l9>=1, s2>=1 -> 
	l9'=l9-1,
	l10'=l10+1;

l10>=1, s2>=1 -> 
	s2'=s2-1,
	s1'=s1+1,
	l10'=l10-1,
	l11'=l11+1;

l11>=1, s2>=1 -> 
	s2'=s2-1,
	s16'=s16+1,
	l11'=l11-1,
	l13'=l13+1;

l0>=1, s3>=1 -> 
	s3'=s3-1,
	s1'=s1+1,
	l0'=l0-1,
	l1'=l1+1;

l0>=1, s3>=1 -> 
	l0'=l0-1,
	l1'=l1+1;

l1>=1, s3>=1 -> 
	s3'=s3-1,
	s2'=s2+1,
	l1'=l1-1,
	l2'=l2+1;

l1>=1, s3>=1 -> 
	l1'=l1-1,
	l2'=l2+1;

l2>=1, s3>=1 -> 
	s3'=s3-1,
	s2'=s2+1,
	l2'=l2-1,
	l3'=l3+1;

l4>=1, s3>=1 -> 
;

l4>=1, s3>=1 -> 
	l4'=l4-1,
	l5'=l5+1;

l5>=1, s3>=1 -> 
	s3'=s3-1,
	s2'=s2+1,
	l5'=l5-1,
	l6'=l6+1;

l6>=1, s3>=1 -> 
	l6'=l6-1,
	l7'=l7+1;

l8>=1, s3>=1 -> 
	l8'=l8-1,
	l9'=l9+1;

l9>=1, s3>=1 -> 
;

l9>=1, s3>=1 -> 
	l9'=l9-1,
	l10'=l10+1;

l10>=1, s3>=1 -> 
	s3'=s3-1,
	s1'=s1+1,
	l10'=l10-1,
	l11'=l11+1;

l11>=1, s3>=1 -> 
	l11'=l11-1,
	l12'=l12+1;

l3>=1, s4>=1 -> 
	s4'=s4-1,
	s0'=s0+1,
	l3'=l3-1,
	l8'=l8+1;

l3>=1, s5>=1 -> 
	s5'=s5-1,
	s1'=s1+1,
	l3'=l3-1,
	l8'=l8+1;

l3>=1, s6>=1 -> 
	s6'=s6-1,
	s2'=s2+1,
	l3'=l3-1,
	l8'=l8+1;

l3>=1, s7>=1 -> 
	s7'=s7-1,
	s3'=s3+1,
	l3'=l3-1,
	l8'=l8+1;

l3>=1, s0>=1 -> 
	s0'=s0-1,
	s4'=s4+1,
	l4'=l4+1;

l3>=1, s1>=1 -> 
	s1'=s1-1,
	s5'=s5+1,
	l4'=l4+1;

l3>=1, s2>=1 -> 
	s2'=s2-1,
	s6'=s6+1,
	l4'=l4+1;

l3>=1, s3>=1 -> 
	s3'=s3-1,
	s7'=s7+1,
	l4'=l4+1;


init
s1=0, s2=0, s3=0, s4=0, s5=0, s6=0, s7=0, s8=0, s9=0, s10=0, s11=0, s12=0, s13=0, s14=0, s15=0, s16=0, l1=0, l2=0, l3=0, l4=0, l5=0, l6=0, l7=0, l8=0, l9=0, l10=0, l11=0, l12=0, l13=0, 
l0>=1, s0=1

target
s16>=1,l13>=1
