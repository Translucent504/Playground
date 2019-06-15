# Vague Ideas to try
- End Goal: Application that allows an image to be taken of an english passage that has some sort of physics mechanics problem. The application then displays a visual simulation of what the passage said.

# Sub problems to solve:
1. write an OCR that can reliably read english text from an image of a textbook.
2. write some application that allows extraction of the necessary physics / mechanical information (state of objects and their relation etc) from any given english passage.
3. make an app that allows to display a mechanics simulation given some objects and their relations.



# Purpose (PhysViz)
- Use camera to capture question / passage.
- Extract information from picture using NLP or whatever.
- Use extracted information to display a picture of what is asked in the question.
- Include the ability to simulate the scene and predict what happens in the future?

# Design questions / problems
- Does something like this exist?
- How to do the OCR from bad photos... or allow manual typing..
- Which library to use to display / simulate:
  - manim?
  - pygame?
  - ????
- How to extract information from the passage?
  - what NLP techniques exist
  - Knowledge graphs / knowledge representation etc...
  - existing libraries?
- allow camera movement?
- 3d perspective or 2d?
  - sideview?
  - top down?
  - wtf is isometric?
- mobile app or desktop app or web app?
- Only for classical mechanics or also electrostatics / springs etc?


# Stuff worth looking at:
- [spaCy](https://spacy.io/) NLP python library
- [socratic](https://socratic.org/) A similar app that does nlp stuff and gives wikipedia like answers and stepwise math solutions but nothing for actual physics mechanics simulation
