def tag(tag, *args, **kwargs):
    if 'html_class' in kwargs.keys():
        kwargs['class'] = kwargs.pop('html_class')
    attrs = ''.join(f'{k}="{v} "' for k, v in kwargs.items())
    # print(attrs if kwargs else 'vazio')
    # print(tag)
    inner = ''.join(args)
    return f'<{tag}{" " if attrs else ""}{attrs}>{inner}</{tag}>'


if __name__ == '__main__':
    tag1 = tag('span', 'Curso de Python 3, por ')
    tag2 = tag('strong', 'Juracy Filho', id='jf')
    tag3 = tag('span', ' e ')
    tag4 = tag('strong', 'Leonardo Leitão', id='ll')
    tag5 = tag('span', '.')
    print(
        tag('p',
            tag1,
            tag2,
            tag3,
            tag4,
            tag5,
            html_class='alert')
    )

"""
<p class="alert"><span>Curso de Python 3, por </span>
<strong id="jf">Juracy Filho</strong><span > e </span>
<strong id="ll">Leonardo Leitão</strong><span >.</span></p>

"""
