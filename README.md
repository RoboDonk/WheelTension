# WheelTension
Wheel Tension Assistant

This application is dedicated to the memory of John Jones. I hope he would have been chuffed to bits by this little idea.

The WheelTension program takes in several numerical inputs obtained by the user as a flexion reading from a Park Tool TM-1 tension meter. WheelTension returns the average spoke tension and the acceptable range of the relative spoke tensions, as described in the TM-1 user manual. 

John Jones taught me a unique approach to building mountainbike (MTB) wheels: Thicker gauge spokes on the driveside; thinner gauge spokes on the non-driveside

The driveside of the wheel experiences more force. Therefore, to John, it made sense to reinforce the driveside with a higher gauge spoke.  I've continued to build my MTB wheels the Jones way, and have ridden them to great satisfaction.

I would like to develop this program so that it is able to differentiate between spoke gauges between the driveside and non-driveside of the wheel.

Park Tool has a robust brower tool for imaging spoke tension that works great for wheels with unifrom gauge spokes. It does not, however, differentiate between  spoke gauges. I would like to fix that, and I've very little idea of how to do it... Baby steps, I guess.


This tool is incomplete:

## TODO:
- Fix input processing from get_spokes_total 
- Create tension meter flexion readings lookup table
- Make tension meter flexion reading getter/setter method

