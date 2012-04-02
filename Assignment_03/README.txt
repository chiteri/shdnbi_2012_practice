Hi Martin,

  So sorry I've been out of touch. This spring was busy. I was interviewing for jobs and was offered a professor position (I am currently a research associate, similar to a post-doc) at Siena College, a small school about 3 hours drive north of New York City. I'll be doing more teaching and continuing my research. My wife is a planetary scientist so we were looking for jobs for her as well in that area and we found her a research position at Rensselaer Polytechnic Institute where we met in grad school, and about 10 minutes from Siena. It's been a very busy, but very exciting month! 

    I looked at all the plots you put on Facebook and they look great! That's exactly how we do research, looking for these ``bumps". Sometimes, the analysis is more sophisticated, but to first order, you've done an analysis!

   Now, let's get a bit more real....   :)

   I've attached a file that has the energy, momentum and charge information of the muons. The beginning of the file looks like this....

2
7.334   2.060   5.886   -3.858  -1
5.208   -1.550  -1.820  4.625    1
2
18.467  8.034   -3.941  -16.154 -1
10.729  6.295   -2.524  -8.313   1

   The first line tells you how many particles to expect for that ``event". In this case we have 2 muons, so you will always see this 2. In more complicated data files, you may have many more particles. 

  The next 5 numbers tell you something about muon 0 and the next 5 numbers tell you something about muon 1. Here's how it breaks down. 

E  px  py  pz  q

  E is the energy of the muon. 
  px, py, and pz are the 3-dimensional components of the momentum. If you haven't been exposed to this before, you may want to review. 

http://en.wikipedia.org/wiki/Cartesian_coordinate_system
http://en.wikipedia.org/wiki/Four-momentum

   q is referring to the electric charge of each muon. 

   So your next exercise to piece the muons back together to see what they came from. This is what I've already done for your first exercise....but now it's up to you.  :)     Remember, it's possible that they muons came from other particles and did not come from the same ``parent" particle. So here's what you want to do. 

   Let's hypothesize that the muons came from a parent ``candidate". ``Candidate" is the term we generally use in particle physics. So you want to get the energy of the candidate (E_c), assuming it decayed to the two muons. Simple! Just add the energy of the muons. 

E_c = E_0  +   E_1

   Same thing for the px, py, pz

px_c  = px_0  +  px_1
.....

   Now you want to calculate the mass of the candidate, according to what Einstein taught us. That should be in that slide of equations.

m^2  =  E^2  -   p^2

   If you've done this correctly, you should get the numbers in that file I sent you. The order is the same. 

   Trust me, this is always a bit tricky. I've messed this up myself before. So give it a shot, and if it's not working, I can always check out your github code and see if I can help.

   
    At this point, I think it's worth thinking about what you want to do for Science Hack Day Nairobi in a couple of weeks. We've gone through quite a bit of learning, both physics and coding, so maybe there's something there. You're going to be the local expert, so what would you like to do? Maybe there's a website that you and the others can put together that walks people through the same exercises that we went through? Or maybe you want to do some other visualizations of the data? I'm not sure....it's your party!  :)

   Let me know if I can be of any help with this exercise. I should be able to respond quicker over the next month. Hope all is well with you, Martin and Morris!