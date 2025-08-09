def create_flex_columns(html1, html2, padding=0):
    return f'''
    <div style="display: flex;">
        <div style="flex: 1; padding: {padding};">
            {html1}
        </div>
        <div style="flex: 1; padding: {padding};">
            {html2}
        </div>
    </div>
    '''
