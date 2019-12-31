FROM python:3
RUN pip install flask
ADD MainScores.py /
ADD Scores.txt /
CMD ["python3" , "./MainScores.py" ]
