Jingle: Michelle Zhu, Amanda Tan
SoftDev
K22: Testing On-Ramps
2024-11-20

DISCO:
1. Tailwind uses the ```<script>``` tag for CDN, while Bootstrap and Foundation use the ```<link>``` tag to import CSS stylesheets.
2. We notice that placeholders are default, light gray fonts that disappear when the user starts typing.
3. Wordings are similar across the three styling tools with slightly different variations. In particular, Foundation and Bootstrap are similar in the naming style of classes.

QCC:
1. Is there a reason why some styling tools prefer the ```<script>``` tag, while others prefer the ```<link>``` tag?
2. We know that Bootstrap was originally developed and used by Twitter, how did Tailwind and Foundation come about?
3. What does data-active-collapse="true" do in Foundation? Nothing changed when we removed it.

q0: 1

q0b: 

https://tailwindcss.com/docs/installation/play-cdn


q1:

We prefer Bootstrap because the wordings are the most straightforward, and the style is minimalistic but visually appealing. Tailwind has many advanced visual features, but most templates are not free. Foundation offers very basic visualization tools, lacking aesthetics.
