FROM frolvlad/alpine-miniconda3

WORKDIR /usr/src/app

COPY conda_requirements.txt /
RUN conda install --file conda_requirements.txt

COPY requirements.txt /
RUN pip install -r /requirements.txt

RUN python -m nltk.downloader punkt

ENV PORT 8080
ENV HOST 0.0.0.0

COPY . /usr/src/app

EXPOSE 8080

CMD ["python", "server.py"]