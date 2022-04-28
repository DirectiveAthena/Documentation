---
copyright: "Andreas Sas 2022"
created: "2022-04-26 02:27"
cssclass: noMetaData
aliases: [No Dependencies]
---
# "No Dependencies" mantra
The following text is written from the perspective of [[Andreas Sas]] to form a better reflection of his thoughts and reasons around the "No Depedency" mantra he has come to form.

---

Hello there and welcome to a glimpse into the madness that I have around this [[Directive Athena]] project of mine. Like a lot I have gotten to myself into, it started out a couple of years ago, way back befode I started streaming.

Back around in 2018 I started out with a "small" cluster of Microsoft Access files which, although cumborsome to maintain, did it's job fairly qell for what it was designed to do. A place to store the early scripts, relations between characters and the world around then, and be a "creative"  place to work in. Now, I never thought I would outgrow the original acceas cluster, but the amount od constrains I began to feel the more I wanted to implement eventually broke the connection that I had with the original cluster.

True to myself, I did struggle around with it dor a lot longer than I really wanted. It took me nearly a year of on and off again usage to finally make a clean break with. "Well... I've used one tool, time for another better one", yeah easier said than done. I had a few things on my list of must haves

- A Relational database (I did try out nosql databases as well, but due to the experience I had with access, I never trully understood the way relations could have worked with a lot of nosal database models)
- A way to store files in a way that they can easily be linked to data on the database.
- Easy retrieval of those files
- Git like tracking of my writing so I never lost another piece of writing 

Now, I did search long and hard for a conhesive solution that would either exsist of one or interwinable ecosystems and... well I couldnt... like at all. I really tried though, gave up on some things I wanted and even then I couldn't find what I needed. I could always find one or more features in a handful of applications but never one that would do it all in an either non proprietary way or able to export the data or link to outside applications.

So now that you know some of the backgrounds we arise at the dawn of the ... let's face it, refactoring hell I find myself in to this day haha. It was around June of 2021 when my [[The Girlfriend|Girlfriend]] made her application final to go to the University of Antwerp to study Physics. With that application she also became aware of the fact that she would need to eventually learn Python, in about a year or so. This, single little thing, made my mind go "huh, programming... I have a little bit of experience with VBA, might actually learn a useful language and help her in the process". Boy was that ever a good and bad decision at the same time.

During the summer I quickly learned the bare basics of Python and by the end of July I made my first gui application by using PySide and ... boy did I fall in love with programming and Python. Now I do know that Python isn't the best language at everything, but it has a healthy community and lots and lots of people making things with it.

Now as you might become aware of, I'm getting awfully close to me starting out with streaming and documenting my work with it. And that is for good reason, as I only came to this "No Dependencies " mantra only right around strating streaming. It was a conscience decision I didn't make light hearted. I didn't really know what the consequences would eventually entail, but I knew it would have more benefits than downsides.

For the actual mantra now. It actually started out with only a few words: "what if I did this myself". I don't even fully remember to what I said it exactly, but I think it had to something with a Mass Ui file converter (not the individual file one, but a simple script to loop over every file and convert all .ui files to .Python files by using the Pyside Pyuic script). Something small I used a package for I now have completely forgotten the name of. But it didn't take me long to build one myself which would do something the "premade" did not, only change edited files and worked quicker because of it!
Now this is where I got the taste, and it was truely formed into a midset a long while later. It took me up until the start of working on [[AthenaColor]] that I truely wanted to make as much as I can myself, to get a true "No dependency" project.

Now to be fair, I know I won't be able to completely do this, as for example I have laid out a rule to not make a game engine form the ground up. The folling list a bunch of things that I said I probably won't do myself, but will rely on something else on:
- A Gui library
- A game engine
- A bot connector library (like Nextcord)
- A database
- ... (see the future for a better and bigger defined list. Or knowing me, a good reason why I eventually decided to make my own database from the ground up)

So I hope that explains it a little bit. I'll probably add to this as the project evolves and make a footnote sections of all important changes to the text here, linking back to the last commit where the text looked like before the mentioned changes