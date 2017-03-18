unzip:
  pkg.installed

send_file:
  file.managed:
      - name: /tmp/apache-maven-${version}-bin.zip
      - source: salt://apache-maven-${version}-bin.zip
      - require:
           - pkg: unzip

extract_file:
  cmd.run:
      - name: unzip apache-maven-${version}-bin.zip
      - cwd: /tmp
      - unless: test -d /tmp/apache-maven-${version}-bin
      - require:
        - file: send_file

make_dir:
  cmd.run:
      - name: mkdir -p /opt/maven
      - unless: test -d /opt/maven/
      - require:
        - cmd: extract_file

move_maven:
  cmd.run:
      - name: mv /tmp/apache-maven-${version}-bin /opt/maven/
      - unless: test -d /opt/maven/apache-maven-${version}-bin
      - require:
        - cmd: make_dir

change_env:
  cmd.run:
      - name: echo 'MAVEN_HOME=/opt/maven/apache-maven-${version}-bin \n PATH=$MAVEN_HOME/bin:$PATH  \n export MAVEN_HOME \n export PATH \n ' >> /etc/profile
      - user: root
      - unless: cat /etc/profile|grep MAVEN
      - require:
        - cmd: move_maven