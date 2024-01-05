from flask_wtf import FlaskForm
from wtforms import Form, PasswordField, BooleanField, SubmitField,StringField,RadioField
from wtforms import SelectField,TextAreaField
from wtforms.validators import DataRequired, Length


class UserForm2(FlaskForm):
    boring = RadioField(
        '您认为哪一张图片更加让您感到无聊？',
        validators=[DataRequired('请选择标签！')],
        choices=[('1', u'左'), ('2', u'右')],
        render_kw={
            'class': 'radio_type',
            'type': 'radio',
            'checked': 'checked',
            'required': 'required'
        },
        coerce=int
    )

    beauty = RadioField(
        '您觉得哪一张图片的景色更加美丽？',
        validators=[DataRequired('请选择标签！')],
        choices=[('1', u'左'), ('2', u'右')],
        render_kw={
            'class': 'radio_type',
            'type': 'radio',
            'checked': 'checked',
            'required': 'required'
        },
        coerce=int
    )

    lively = RadioField(
        '您觉得哪一张图片更加热闹？',
        validators=[DataRequired('请选择标签！')],
        choices=[('1', u'左'), ('2', u'右')],
        render_kw={
            'class': 'radio_type',
            'type': 'radio',
            'checked': 'checked',
            'required': 'required'
        },
        coerce=int
    )

    depressing = RadioField(
        '您认为哪一张图片更加让您感到压抑？',
        validators=[DataRequired('请选择标签！')],
        choices=[('1', u'左'), ('2', u'右')],
        render_kw={
            'class': 'radio_type',
            'type': 'radio',
            'checked': 'checked',
            'required': 'required'
        },
        coerce=int
    )

    safe = RadioField(
        '您认为哪一张图片更加让您感到安全？',
        validators=[DataRequired('请选择标签！')],
        choices=[('1', u'左'), ('2', u'右')],
        render_kw={
            'class': 'radio_type',
            'type': 'radio',
            'checked': 'checked',
            'required': 'required'
        },
        coerce=int
    )

    onclick = "alert('成功')"
    submit = SubmitField('保存并提交', render_kw={'onclick': 'alert("调查问卷已成功提交，感谢您的参与！")'})

