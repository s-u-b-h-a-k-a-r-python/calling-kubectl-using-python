FROM python:3.9.0-buster



ARG VCS_REF
ARG BUILD_DATE

LABEL org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.name="calling-kubectl-using-python" \
      org.label-schema.url="https://hub.docker.com/r/subhakarkotta/calling-kubectl-using-python/" \
      org.label-schema.vcs-url="https://github.com/subhakarkotta-python/calling-kubectl-using-python" \
      org.label-schema.build-date=$BUILD_DATE

ENV KUSTOMIZE_VER 3.8.2
ENV KUBECTL_VER 1.19.3


RUN curl -L https://storage.googleapis.com/kubernetes-release/release/v${KUBECTL_VER}/bin/linux/amd64/kubectl -o /usr/local/bin/kubectl \
    && chmod +x /usr/local/bin/kubectl
      
RUN curl -L https://github.com/kubernetes-sigs/kustomize/releases/download/v${KUSTOMIZE_VER}/kustomize_${KUSTOMIZE_VER}_linux_amd64  -o /usr/local/bin/kustomize \
    && chmod +x /usr/local/bin/kustomize

RUN pip install requests

ADD lib/ /lib
ADD ssh/ /root/.ssh

ADD run.py /run.py

CMD [ "python3", "./run.py" ]


