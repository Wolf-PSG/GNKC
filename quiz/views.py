from django.http.response import Http404
from django.shortcuts import redirect, render, get_object_or_404, get_list_or_404
from .models import Question, Quiz
from teachers.models import Teacher
from quiz.form import quizForm
from quiz.questionForm import questionForm


def quiz(request, quizID):
    try:
        quiz = get_object_or_404(Quiz, id=quizID)
        print(request.user.id)
        print(quiz.teacher_id)
        print(quiz.classes)
        print(quiz.level)
    except:
        print('whoops 3')
        return redirect('index')

    if request.user.is_authenticated:
        try:
            if (request.user.classes == quiz.classes) & (request.user.level == quiz.level) & (request.user.teacher == quiz.teacher_id):
                questionList = get_list_or_404(Question, quiz=quizID)
                context = {
                    'questions': questionList
                }
                print(context)
        except:
            if (request.user.id == quiz.teacher_id):
                questionList = get_list_or_404(Question, quiz=quizID)
                context = {
                    'questions': questionList,
                    'quiz': quizID
                }
                print(context)

                return render(request, 'quiz/quiz.html', context)
    else:
        return redirect('index')


def create(request):
    form = quizForm()
    addQuestionForm = questionForm()
    if request.user.is_authenticated & request.user.is_staff:
        if request.method == 'POST':
            print(request.user.id)
            teacher_id = Teacher.objects.select_related(
                'user').get(user_id=request.user.pk)
            print(teacher_id.pk)
            print(request.POST)
            quizSubmit = quizForm(request.POST, request.FILES)
            print(quizSubmit)
            if quizSubmit.is_valid():
                print('valid')
                quiz_form_submit = quizSubmit.save(commit=False)
                quiz_form_submit.teacher_id = teacher_id.pk
                quiz_form_submit.save()
                quiz_id = quiz_form_submit.pk
                print(quiz_id)
                # return redirect('quizzes')
                return render(request, 'question/question.html', {'id': quiz_id, 'form': addQuestionForm})

            return redirect('quizzes')
        return render(request, 'quiz/createQuiz.html', {'form': form})
    return render(request, 'quiz/createQuiz.html', {'form': form})


def addQuestion(request):
    addQuestionForm = questionForm()
    if request.user.is_authenticated & request.user.is_staff:
        if request.method == 'POST':
            print(request.POST)
            questionSubmit = questionForm(request.POST, request.FILES)
            quizID = request.POST['quiz_id']
            quizInstance = get_object_or_404(Quiz, pk=quizID)
            if questionSubmit.is_valid():
                question_form_submit = questionSubmit.save(commit=False)
                question_form_submit.quiz = quizInstance
                question_form_submit.save()
                try:
                    quiz_Questions = get_list_or_404(Question, quiz_id=quizID)
                    context = {
                        'questions': quiz_Questions,
                        'id': quizID,
                        'form': addQuestionForm
                    }
                except Http404:
                    context = {
                        'id': quizID,
                        'form': addQuestionForm
                    }
                return render(request, 'question/question.html', context)
            print('no work')
            return render(request, 'question/question.html', {'id': quizID, 'form': addQuestionForm})
        return redirect('quizzes')
    return redirect('quizzes')


def delete(request, questionID):
    addQuestionForm = questionForm()
    if request.user.is_authenticated & request.user.is_staff:
        question = Question.objects.get(id=questionID)
        quizID = question.quiz_id
        question.delete()
        return render(request, 'question/question.html', {'id': quizID, 'form': addQuestionForm})


def deleteQuiz(request, quizID):
    if request.user.is_authenticated & request.user.is_staff:
        quiz = Quiz.objects.get(id=quizID)
        quiz.delete()
        return redirect('quizzes')
    return redirect('index')


def updateQuiz(request, quizID):
    if request.user.is_authenticated & request.user.is_staff:
        try:
            quiz = get_object_or_404(Quiz, id=quizID)
        except:
            print('whoops 3')
            return redirect('index')
        try:
            questionList = get_list_or_404(Question, quiz=quizID)
            context = {
                'questions': questionList
            }
            print(context)
        except:
            return redirect('index')
    return redirect('index')


def updateQuestion(request, questionID):
    return redirect('index')


def submit(request):
    # TODO make it so if the question is wrong -- add it to a dict and show on page.
    if request.method == 'POST':
        score = 0
        wrongAnswerList = []
        print(request.POST)
        submitted = {answer: request.POST[answer] for answer in request.POST.keys(
        ) - {'csrfmiddlewaretoken', 'id'}}
        print(submitted)

        for id in submitted:
            question = get_object_or_404(Question, id=id)
            if (str(question.correct_answer) == submitted[id]):
                score = score + 1
            else:
                wrongAnswerList.append(question)

        context = {
            'wrongAnswer': wrongAnswerList,
            'score': score
        }
        return render(request, 'quiz/submitted.html', context)
    return redirect('quizzes')
