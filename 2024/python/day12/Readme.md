# Approach
we want to count faces / edges around the area.

- we start at a 2 faced or 3 faced corner to make counting the faces easier (we could also start at a straight edge which is fine too)

- we start by counting the start faces (foreign areas around the start area) and subtract 1 because we count that when we end up there again.

- we start walking in one direction (figure out)

- we detect a bend (left or right) (no foreign area around -> bend and move) (next area is foreign -> bend and don't move)

- when we move, we add the next area to our seen set

- we take that bend and add 1 to our faces. (before we check if we have seen the next area)

- after we counted our bend (that's why we subtracted 1 at the beginning), we check if we ended up at the start again.

- we can only add areas to our seen set if they are part of the border -> problem we have a narrow 1 area path => we note down our start and not every area we've passed.


I believe this works for 2 faced bends, 3 faced bends and 4 faced areas
- what if we detect more bends than there are faces here? should we not start with going one direction and count every bend even if it's a 4 faced area.
We would just turn around 4 times and finish with 4 bends = 4 faces
