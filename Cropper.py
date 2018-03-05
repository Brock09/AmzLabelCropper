
# coding: utf-8

# In[1]:


from PyPDF2 import PdfFileReader, PdfFileWriter


# In[2]:


myFile1 = PdfFileReader('package.pdf', 'r')
myFile2 = PdfFileReader('package.pdf', 'r')


# In[3]:


pageWriter = PdfFileWriter()


# In[4]:


for i in range(myFile1.getNumPages()):
    labelOne = myFile1.getPage(i)
    labelOne.cropBox.setLowerLeft((20,750))
    labelOne.cropBox.setUpperRight((250,400))
    labelTwo = myFile2.getPage(i)
    labelTwo.cropBox.setLowerLeft((28,370))
    labelTwo.cropBox.setUpperRight((490,61))
    pageWriter.addPage(labelOne)
    pageWriter.addPage(labelTwo)


# In[5]:


outstream = open('package_cropped.pdf', 'wb')
pageWriter.write(outstream)
outstream.close()

