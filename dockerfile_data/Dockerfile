# 베이스 이미지
FROM ubuntu:22.04

# 메타데이터 추가
LABEL maintainer="PSC guppy13567@gmail.com"

# 시스템 업데이트( && - 앞에 내용이 끝나면 이어서 작동하라, \ - 엔터치고 내려가겠다)
RUN apt update -y && \
       apt install -y sudo passwd openssh-server wget && \
       apt install -y nano net-tools iputils-ping && \
       apt install -y openjdk-8-jdk python3-pip && \
       apt clean && \
       apt clean && \
       rm -rf /var/lib/apt/list/* 

# 계정생성 및 세팅
RUN groupadd ppsc && useradd -m -d /home/ppsc -s /bin/bash -g ppsc -G sudo ppsc && \
       echo "ppsc:1234" | chpasswd && \
       mkdir -p /home/ppsc/.ssh && \
       chown -R ppsc.ppsc /home/ppsc && \
       echo "export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64" >> /home/ppsc/.bashrc && \
       echo "export PATH=$PATH /home/ppsc/.local/bin"
       chown ppsc:ppsc /home/ppsc/.bashrc && \
       mkdir -p /var/run/sshd && \
       echo "perminRootLogin no" >> /etc/ssh/sshd_config && \
       echo "PasserdAuthentication yes" >> /etc/ssh/sshd_config

# 사용자 변경
USER ppsc

# 작업환경 변경
WORKDIR /home/ppsc

# pip업그레이드 및 주피터랩 설치
RUN pip install --upgrade pip && pip install jupyterlab

# ssh 서버 실행및 주피터랩 가동(외부접속가능)
CMD ["/bin/bash","-c","service ssh start && python3 -m jupyterlab --ip=0.0.0.0 --port=8888 --allow-root"]