from allauth.account.adapter import DefaultAccountAdapter


class CustomAccountAdapter(DefaultAccountAdapter):

    def send_mail(self, template_prefix, email, context):
        # hashed = hashlib.sha256(str(context['key']).encode('utf-8')).hexdigest()
        # code = int(hashed, 16) & (10 ** 6)
        context['activate_url'] = context['key']
        msg = self.render_mail(template_prefix, email, context)
        msg.send()
