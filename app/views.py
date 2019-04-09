from flask import render_template, flash, redirect, request
from werkzeug.utils import secure_filename

from app import forms
from app import app
import matplotlib.pyplot as plt


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/kvadraturav', methods=['GET', 'POST'])
def kurav():
    form = forms.Kurav()
    if form.validate_on_submit():
        az =float(form.a.data)
        bz = float(form.b.data)
        cz = float(form.c.data)
        if bz == 0 and cz == 0:
            flash('x = 0')
        else:
            if az == 0 and bz == 0:
                flash('Это не уравнение')
            elif az == 0:
                x = cz / bz
                flash('Это не квадратное уравнение, но '
                      'x = ' + str(x))
            else:
                d = bz ** 2 - 4 * az * cz
                flash('D = b^2 - 4ac =' + str(bz) + '^2 - 4*' + str(az) + '*' + str(cz) + '= ' + str(d))
                if d < 0:
                    flash('Решений нет')
                if d == 0:
                    x = -(bz / 2 * az)
                    flash('Только одно решение: х = ' + str(x))
                if d > 0:
                    x1 = (-bz - d ** 0.5) / (2 * az)
                    x2 = (-bz + d ** 0.5) / (2 * az)
                    flash('Есть 2 решения: x1 = ' + str(x1) + ' x2 = ' + str(x2))
    return render_template('kurav.html', form=form)


@app.route('/right_triangle', methods=['GET', 'POST'])
def right_triangle():
    form = forms.Kurav()
    if form.validate_on_submit():
        az = float(form.a.data)
        bz = float(form.b.data)
        cz = float(form.c.data)
        if az < 0 or bz < 0 or cz < 0:
            flash('Вы не правильно ввели значения')
        if az == 0:
            a = cz ** 2 + bz ** 2
            az = a ** 0.5
            flash('А = корень из ' + str(a) + 'или А = ' + str(az))
        if bz == 0:
            b = az ** 2 + cz ** 2
            bz = b ** 0.5
            flash('В = корень из ' + str(b) + ' или В = ' + str(bz))
        if cz == 0:
            c = az ** 2 + bz ** 2
            cz = c ** 0.5
            flash('C = корень из ' + str(c) + 'или С = ' + str(cz))
        p = (az + bz + cz) / 2
        Sz = (p * (p - az) * (p - bz) * (p - cz))
        S = (p * (p - az) * (p - bz) * (p - cz)) ** 0.5
        if S == 0:
            flash('Такого треугольника не существует')
        else:
            flash('Полупериметр = ' + str(p))
            flash('S = корень из ' + str(Sz) + ' или S =' + str(S))
            ha = S * 2 / az
            hb = S * 2 / bz
            hc = S * 2 / cz
            flash('Высота к A = ' + str(ha))
            flash('Высота к B = ' + str(hb))
            flash('Высота к C = ' + str(hc))
    return render_template('prtriagle.html', form=form)


@app.route('/pltriagle', methods=['GET', 'POST'])
def pltriagle():
    form = forms.Treagle_on_ploskost()
    if form.validate_on_submit():
        ax = float(form.ax.data)
        ay = float(form.ay.data)
        bx = float(form.bx.data)
        by = float(form.by.data)
        cx = float(form.cx.data)
        cy = float(form.cy.data)
        y_ = bx
        x_ = ax
        y_1 = by
        x_1 = ay
        c_ = cx
        c_1 = cy
        AB = ((y_ - x_) ** 2 + (y_1 - x_1) ** 2) ** 0.5
        BC = ((y_ - c_) ** 2 + (y_1 - c_1) ** 2) ** 0.5
        CA = ((c_ - x_) ** 2 + (c_1 - x_1) ** 2) ** 0.5
        p = (AB + BC + CA) / 2
        S = (p * (p - AB) * (p - BC) * (p - CA)) ** 0.5

        if y_ > c_:
            ma1 = (y_ + c_) / 2
        else:
            ma1 = (c_ + y_) / 2
        if y_1 > c_1:
            ma2 = (y_1 + c_1) / 2
        else:
            ma2 = (c_1 + y_1) / 2
        if x_ > c_:
            mb1 = (x_ + c_) / 2
        else:
            mb1 = (c_ + x_) / 2
        if x_1 > c_1:
            mb2 = (x_1 + c_1) / 2
        else:
            mb2 = (c_1 + x_1) / 2
        if x_ > y_:
            mc1 = (x_ + y_) / 2
        else:
            mc1 = (y_ + x_) / 2
        if x_1 > y_1:
            mc2 = (x_1 + y_1) / 2
        else:
            mc2 = (y_1 + x_1) / 2

        ma = ((ma1 - ax) ** 2 + (ma2 - ay) ** 2) ** 0.5
        mb = ((mb1 - bx) ** 2 + (mb2 - by) ** 2) ** 0.5
        mc = ((mc1 - cx) ** 2 + (mc2 - cy) ** 2) ** 0.5
        ha = 2 / AB * S
        hb = 2 / BC * S
        hc = 2 / CA * S
        Lc = (2 * ((CA * BC * p * (p - AB)) ** 0.5)) / (CA + BC)
        La = (2 * ((AB * CA * p * (p - BC)) ** 0.5)) / (AB + CA)
        Lb = (2 * ((AB * BC * p * (p - CA)) ** 0.5)) / (AB + BC)
        flash('AB  = ' + str(AB))
        flash('BC  = ' + str(BC))
        flash('CA  = ' + str(CA))
        flash('Полупериметр = ' + str(p))
        flash('Площадь = ' + str(S))
        flash('Высота к А = ' + str(ha))
        flash('Высота к В = ' + str(hb))
        flash('Высота к С = ' + str(hc))
        flash('Бессектриса угла A к противолежайщей стороне = ' + str(La))
        flash('Бессектриса угла B к противолежайщей стороне = ' + str(Lb))
        flash('Бессектриса угла C к противолежайщей стороне = ' + str(Lc))
        flash('Медиана к стороне A = ' + str(ma))
        flash('Медиана к стороне B = ' + str(mb))
        flash('Медиана к стороне C = ' + str(mc))
        fig = plt.figure()
        print(fig.axes)
        print(type(fig))
        plt.scatter(ax, ay)
        plt.scatter(bx, by)
        plt.scatter(cx, cy)
        plt.scatter(ma1, ma2)
        plt.scatter(mb1, mb2)
        plt.scatter(mc1, mc2)
        plt.text(ma1, ma2, 'a')
        plt.text(mb1, mb2, 'b')
        plt.text(mc1, mc2, 'c')
        plt.plot([bx, ax], [by, ay])
        plt.plot([cx, bx], [cy, by])
        plt.plot([ax, cx], [ay, cy])
        plt.text(ax, ay, 'A')
        plt.text(bx, by, 'B')
        plt.text(cx, cy, 'C')
        print(fig.axes)
        grid1 = plt.grid(True)
        with open('triagle.pdf', 'w') as file:
            with open('triagle.png', 'w') as file:
                plt.show()

    return render_template('pltriagle.html', form=form)

