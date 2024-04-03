# Foundational skills
math_and_stats = Skill("Foundational Mathematics and Statistics", ["Linear Algebra", "Calculus", "Probability and Statistics", "Discrete Mathematics"])
programming = Skill("Programming and Computational Skills", ["Python", "R", "JavaScript", "Data Structures", "Algorithms"])
devops = Skill("DevOps Skills", ["AWS", "Docker", "Git"])

# Core areas
cognitive_psychology = Skill("Cognitive Psychology", prerequisites=[math_and_stats.name])
neuroscience = Skill("Neuroscience", prerequisites=[math_and_stats.name])
machine_learning = Skill("Machine Learning and Neural Networks", prerequisites=[programming.name, math_and_stats.name])
philosophy_of_mind = Skill("Philosophy of Mind")

# Advanced areas
advanced_cognitive_psychology = Skill("Advanced Topics in Cognitive Psychology", prerequisites=[cognitive_psychology.name])
computational_neuroscience = Skill("Computational Neuroscience", prerequisites=[neuroscience.name, programming.name])
deep_learning = Skill("Deep Learning", prerequisites=[machine_learning.name])
ai_ethics = Skill("AI Ethics and Society", prerequisites=[philosophy_of_mind.name, machine_learning.name])

# Defining Learning Paths
lp_cognitive_science = LearningPath("Cognitive Science and Neuroscience Path", [cognitive_psychology, neuroscience, advanced_cognitive_psychology, computational_neuroscience])
lp_ai_development = LearningPath("AI Development and Ethics Path", [programming, devops, machine_learning, deep_learning, ai_ethics])

# Adding skills to paths and listing them
lp_cognitive_science.list_skills()
lp_ai_development.list_skills()
