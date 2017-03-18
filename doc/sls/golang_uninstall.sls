rm_tmpgo:
  cmd.run:
      - name: rm -Rf ./go${version}.linux-amd64.tar.gz
      - cwd: /tmp

rm_go:
  cmd.run:
      - name: rm -Rf /opt/go

rm_gopath:
  cmd.run:
      - name: rm -Rf /opt/gopath

rm_go_profile:
  cmd.run:
      - name: sed -i '/^GO*/d' /etc/profile