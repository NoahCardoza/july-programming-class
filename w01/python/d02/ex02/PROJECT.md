# Exercise 2: Assignment

You are the commander of the ion cannon at the Rebel base on the ice-planet of Hoth. Luke Skywalker
and Han Solo have just warned you that the Empire knows where you are, and sure enough `five` Imperial
Starships have just appeared in our sector. Luckily they came out of hyperspace farther away than they
wanted (I bet Vader’s not happy about that) so you have a little bit of a warning. Right now (`time zero`) they are
`8500` km away and closing at different speeds. You need to hit each ship as it comes within range. That
should give the Imperials enough trouble to deal with while you evacuate the base.

The ion cannon needs `180 seconds` to charge up before you can start firing, and it can only hit things
within `1000km`. You need to calculate the time at which to start charging it up so it can fire at each ship
just as they get within `1000km`.

Assignment: write a fire-control program for the ion cannon.

1. Ask the user for their identifier. If they answer anything other
than "CMDR" then tell them they’re unauthorized and quit the
program. We can’t have unauthorized users firing the ion cannon!

2. Using a `for` loop:
    1. Ask the user for the speed of the next incoming ship.

    2. Calculate how long until the ship gets within `1000 km` of Hoth: that’s when you should fire at it. Output this time
     estimate to the user so they know when to fire at each ship.

    3. If any ship will get to Hoth before you can fire the cannon then there’s no point charging the cannon. If the calculation suggests this is the case, tell the commander immediately to get out of the base! Then quit the program – there’s no point asking about the rest of the incoming ships.

Useful equation: `time = distance / speed`
