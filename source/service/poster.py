class Poster:

    def run_poster(self, target, news):
        target.connect()
        for new in news:
            if target.can_post(new):
                target.post_new(new)
                print('Postada-->', new.title)
            else:
                print('Repetida-->', new.title)