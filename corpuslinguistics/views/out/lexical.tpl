<html>
{% include 'main_view.tpl' %}
   <body>
     <h1>{{ name }}</h1>
   </br>
     <table>
        <tr>
          <th>Word&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</th>
          <th>Count</th>
        </tr>
        {% for row in rows %}
        {% set x = row.split() %}
        <tr>
            <td>{{ " ".join(x[0:2]) }}&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td>

            <td>{{ x[-1]}}</td>
         </tr>
        {% endfor %}
     </table>
</body>
