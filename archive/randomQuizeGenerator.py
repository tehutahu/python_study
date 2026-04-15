#! python3
# ランダムな順に問題と答えを並べて問題集と回答集を作る

import os, random

# data
capitals = {'北海道': '札幌市', '青森県': '青森市', '岩手県': '盛岡市',
            '東京都': '東京', '京都府': '京都市', '沖縄県': '沖縄市'}

for quiz_num in range(3):
    # quiz and answer
    quiz_file = open('capitalsquiz{}.txt'.format(quiz_num+1), 'w')
    answer_key_file = open('capitalsquiz_answer{}.txt'.format(quiz_num+1), 'w')

    # make header
    quiz_file.write('Name:\n\nDate:\n\nClass:\n\n')
    quiz_file.write((' ' * 20) + 'capitalsquiz(Number{})'.format(quiz_num+1))
    quiz_file.write('\n\n')

    # shuffle capital key list
    prefectures = list(capitals.keys())
    random.shuffle(prefectures)

    # make quiz
    for question_num in range(len(prefectures)):
        # correct and wrong
        correct = capitals[prefectures[question_num]]
        wrong = list(capitals.values())
        del wrong[wrong.index(correct)]
        wrong = random.sample(wrong, 3)
        answers = wrong + [correct]
        random.shuffle(answers)

        # write quiz statement
        quiz_file.write('{}.{}の県庁所在地は？\n'.format(question_num+1, prefectures[question_num]))
        quiz_file.write('A:{}, B:{}, C:{}, D:{}\n\n'.format(answers[0], answers[1], answers[2], answers[3]))

        # write answer statement
        answer_key_file.write('{}. {}\n'.format(question_num+1, 'ABCD'[answers.index(correct)]))

    quiz_file.close()
    answer_key_file.close()
