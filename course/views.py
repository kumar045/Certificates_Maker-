from django.shortcuts import render
import pandas
from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML
import tempfile
import os





# # Create your views here.
# def learn_django(request):
#   certificate_df = pandas.read_csv('C:\\Users\\Skillup 112\\django\\Project_Skillup\\gs17\\course/example.csv')
#   details =  certificate_df.to_dict('records')
#   print(details[0])

#   return render(request, 'course/home.html', details[0])

  # Create your views here.
def learn_django(request):
  certificate_df = pandas.read_csv('C:\\Users\\Skillup 112\\django\\Project_Skillup\\Certificate_Maker\\course/example.csv')
  details =  certificate_df.to_dict('records')
  Total_Certificates=len(details)
  print(details[0])
  for i in range(Total_Certificates):

    # Rendered
    html_string = render_to_string('course/home.html',details[i] )
    pdf = HTML(string= html_string).write_pdf()
    

    if os.path.exists("gs17/Certificates"):

        f = open(os.path.join("gs17/Certificates", 'certificate'+str(i)+'.pdf'), 'wb')
        f.write(pdf)
    
  # Creating http response
  # response = HttpResponse(content_type='application/pdf;')
  # response['Content-Disposition'] = 'inline; filename=certificate.pdf'
  # response['Content-Transfer-Encoding'] = 'binary'
  # with tempfile.NamedTemporaryFile(delete=True) as output:
  #   output.write(pdf)
  #   output.flush()
  #   output.seek(0)
  #   response.write(output.read())
  return HttpResponse("Generated Now You Can Collect All Certificates From Certificates Folder")

 