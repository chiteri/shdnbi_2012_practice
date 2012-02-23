Hi Martin,


I have attached the solution with some of the adjustments you
recommended. Am still wrapping my head around the concept of bins on
histograms but I think with only the data range included, the values
plotted have been emphasised sufficiently.


   Great! This looks fantastic!

  Yes, histograms and bin widths can be a challenging idea. There's actually quite a bit of information in how you choose to bin your data and how your data 
  looks when you bin it differently. Let me give you an example to try to explain this concept. 

   Suppose I ask you to go to the grocery store to study the prices of items (I'm going to use US$ because that is what I am familiar with). So you go and you 
   just write down the prices of items in the aisle with drinks: soda, fruit juice, etc. You may see prices like $0.75, $1.25, $2.40, $2.30, $0.99, $1.20 .... 
   and so on. Now you go to histogram these data and you have to choose a bin width. If you choose your width to be $10.00 that means everything with a price 
   between $0.00 and $10.00 goes in the first bin, everything with a price of $10.00 and $20.00 goes in the second bin, and on and on. If you bin, this way, 
   then _all_ your drinks go in the first bin and nothing in the other bins. Does this tell you anything? Well, it tells you that all the drinks cost less than 
   $10.00!
   
   But suppose your bin width is $0.10. Now you see that there are some drinks which sell for $1.90 and some that sell for $2.05 and some that sell for $2.11. 
   And maybe there's _a lot_ of drinks that sell for $1.50 and very few for $1.60, but that's good information!

  At the other end of the spectrum, it wouldn't make sense to bin in width of $0.001, because that is less than the smallest unit of money, 1 penny ($0.01). 

   
 
I have a repository for the assignments on Github too [
https://github.com/chiteri/shdnbi_2012_practice/ ]. I could be placing
the contents of the assignments here for you to assess instead of
attaching the files with my workings on e-mail?


   Absolutely! That's a great idea!

   So let me tell you about your plots. First, these look great! OK, here's what the two sets of data are:

1) When the LHC collides protons, there is a massive spray of particles that comes from the collision. There's about 5 or 6 particles that we measure directly, 
as they pass through the CMS detector. The other types of particle live for such a short period of time, that they decay (turn into) other particles very quickly. 
One type of these particles that we _do_detect is the muon. 

http://en.wikipedia.org/wiki/Muon

  The data I sent you are from events where two muons (plus a lot of other stuff) was seen in the collision. When the energy and momentum of the muons are 
  measured by the detectors, they _can be added together_ to determine if they came from a parent particle!

2) There are two ways to relate energy, momentum, mass, and velocity: the Classical method, developed by Isaac Newton in the 1600's; and the Special Relativity 
method, developed by Albert Einstein in 1905. 

   I've attached a .pdf file from a talk I've given that shows the different equations. If you don't understand these quantities, that's OK! :)  It's not 
   important right now (but later we'll discuss this in more detail). For now, just know that the two files I sent you are the ``mass" of the two combined muons 
   calculated in the Classical way and the Special Relativity way. 

   We know that Special Relativity is the more accurate way to do these calculations at these energies at the LHC, so one of those datasets (files) should look 
   more ``interesting" than the other.

3) Let's look for some particles! I know that there is a particle called the J/Psi which likes to decay to muons. There is a similar particle called the Upsilon 
that does the same and another called the Z. 

   These numbers are in units of energy called GeV/c^2. A GeV is a giga-electronvolt, or 1 billion electronvolts. The c^2 is the speed of light squared, which 
   we need to keep the units correct. 
 
   In these units, the mass of a proton is about 1 GeV/c^2 (it's actually 0.938 GeV/c^2, but 1 is good enough for now). The particles I mentioned above are about
   3.1 (J/Psi), 9.5 (Upsilon), and 90 (Z) GeV/c^2. So here's my next challenge: find these particles!

   You'll have to make new plots that ``zoom in" on these regions, and you'll want to rebin the data in those regions. One of those files should show a peak, or 
   extra events, at those masses. That one will be the masses that were calculated with Special Relativity. 

   For instance, when you look for the J/Psi, plot the data on a range from 2.0 to 4.0 and use about 50 or 100 bins. What do you see?
 
   Looking forward to seeing what you discover!
.
-- 
-- 
----------------------------
Matt Bellis
Northern Illinois University
mbellis@niu.edu
bellis@slac.stanford.edu
http://www.mattbellis.com
(cell)    412-310-4586
----------------------------