from flask import Blueprint, render_template, request, flash
from sqlalchemy.orm import sessionmaker
from .forms import Shortner
from app.models import Urls, UrlStat
from app.extensions import db

short_url = Blueprint('short_url', __name__, template_folder='../templates/sh_url')
session_db = sessionmaker(db)


@short_url.route('/', methods=['GET', 'POST'])
def short():
    form = Shortner()
    if request.method == "POST":

        if form.validate_on_submit():
            url_base = request.form.get('URL')
            url_short = request.form.get('shortner_name')
            exist_url = Urls.quety.filter(sh_url=url_short)
            tag = request.form.get('tag_name', None)
            if exist_url:
                flash("Название ссылки занято, выберите новое или оставьте поле пустым для автогенерации.")
                return render_template('short.html', form=form)
            else:
                new_url = Urls(url=url_base, sh_url=url_short, tag=tag)
                session_db.add(new_url)
                session_db.commit()
                pass #TODO

            flash('Новая ссылка готова - sh.su/{}'.format(url_short))
        return render_template('short.html', form=form)

    return render_template('short.html', form=form)
