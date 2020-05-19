import clips
import NLP_processing as nlp


example = ['Humans are mortal.', 'Socrates is a human', 'Socrates is a mortal']


def run_CLIPS(input):
    premise_types = nlp.get_premise_types(input)
    env = clips.Environment()
    env.clear()

    rule = f"""
    (defrule my-rule
      =>
        (assert (premisa1 {premise_types[0]}))
        (assert (premisa2 {premise_types[1]}))
        (assert (concluzia {premise_types[2]}))
        (assert (Running))
      )
    """
    env.build(rule)

    env.batch_star("Proiect.clp")
    env.reset()
    env.run()

    for fact in env.facts():
        print(fact)

    # for rule in env.rules():
    #     print(rule)



run_CLIPS(example)