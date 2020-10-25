FROM subhakarkotta/python-kubectl-kustomize:3-1.19.3-3.8.2

ARG VCS_REF
ARG BUILD_DATE

LABEL org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.name="python-kubectl-kustomize" \
      org.label-schema.url="https://hub.docker.com/r/subhakarkotta/calling-kubectl-using-python/" \
      org.label-schema.vcs-url="https://github.com/subhakarkotta-python/calling-kubectl-using-python" \
      org.label-schema.build-date=$BUILD_DATE

ADD lib/ /lib
ADD ssh/ /root/.ssh

ADD run.py /run.py

CMD [ "python3", "./run.py" ]
