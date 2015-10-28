from hermes.forms import CollectionForm


def include_login_form(request):
    from django.contrib.auth.forms import AuthenticationForm
    form = AuthenticationForm()
    form.fields['username'].widget.attrs['class'] = 'form-control input-lg'
    form.fields['username'].widget.attrs['placeholder'] = 'Username'

    form.fields['password'].widget.attrs['class'] = 'form-control input-lg'
    form.fields['password'].widget.attrs['placeholder'] = 'Password'

    collection_form = CollectionForm()
    return {
        'login_form': form,
        'collection_form': collection_form,
    }