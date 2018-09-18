srb_notebooks = 'https://git.osd.surfsara.nl/srb/notebooks'
track_2 = 'https://git.osd.surfsara.nl/srb/notebooks-track2-big-data-analytics'
vis = 'https://git.osd.surfsara.nl/casperl/InfoVisCursus'

host = 'haukur-test.jove.surfsara.nl'
repo = srb_notebooks
branch = 'master'
action = '/hub/user-redirect/git-pull?'
sub_path = 'track1-unix-cluster/cartesius-demo.md'

print(''.join([host, action, '='.join(['repo', repo]), '&', '='.join(['branch', branch]), '&', '='.join(['subPath', sub_path])]))