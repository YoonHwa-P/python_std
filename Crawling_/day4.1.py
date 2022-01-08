import pandas as pd

html = '''
<table>
    <thead>
        <tr>
            <th>날짜</th>
            <th>종가</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>2022.01.06</td>
            <td>672,000</td>
        </tr>
        <tr>
            <td>2022.01.05</td>
            <td>664,000</td>
        </tr>
        <tr>
            <td>2022.01.04</td>
            <td>644,000</td>
        </tr>
    </tbody>
</table>'''

if __name__ == "__main__":
    print(pd.read_html(html))