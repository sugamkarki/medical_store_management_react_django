from django.shortcuts import get_object_or_404, render
from rest_framework import viewsets

# Create your views here.
from rest_framework.response import Response

from DjangoMedicalApp.models import Company, CompanyBank, MedicalDetails, Medicine
from DjangoMedicalApp.serializers import CompanyBankSerializer, CompanySerializer, MedicalDetailsSerializer, MedicineSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
#
# class CompanyViewSet(viewsets.ModelViewSet):
#     queryset = Company.objects.all()
#     serializer_class = CompanySerializer


class CompanyViewSet(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication, ]
    permission_classes = [IsAuthenticated]

    def list(self, request):
        company = Company.objects.all()
        serializer = CompanySerializer(
            company, many=True, context={"request": request})
        response_dict = {
            "error": False, "message": "All Company List Data", "data": serializer.data}
        return Response(response_dict)

    def create(self, request):
        try:
            serializer = CompanySerializer(
                data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            response_dict = {"error": False,
                             "message": "Company Data Saved Successfully"}
        except:
            response_dict = {"error": False,
                             "message": "Error. Couldn't save data"}
        return Response(response_dict)

    def update(self, request, pk=None):
        try:
            queryset = Company.objects.all()
            company = get_object_or_404(queryset, pk=pk)
            serializer = CompanySerializer(
                company, data=request.data, context={"request", request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            response_dict = {"error": False,
                             "message": "Data updated successfully"}

        except:
            response_dict = {"error": False, "message": "Error while updating"}
        return Response(response_dict)


class CompanyBankViewSet(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication, ]
    permission_classes = [IsAuthenticated]

    def create(self, request):
        try:
            serializer = CompanyBankSerializer(
                data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            response_dict = {"error": False,
                             "message": "Company Bank Data Saved Successfully"}
        except:
            response_dict = {"error": False,
                             "message": "Error. Couldn't save Company Bank data"}
        return Response(response_dict)

    def list(self, request):
        companybank = CompanyBank.objects.all()
        serializer = CompanyBankSerializer(
            companybank, many=True, context={"request": request})
        response_dict = {
            "error": False, "message": "All Company Bank List Data", "data": serializer.data}
        return Response(response_dict)

    def retrieve(self, request, pk=None):
        queryset = CompanyBank.objects.all()
        companybank = get_object_or_404(queryset, pk=pk)
        serializer = CompanyBankSerializer(
            companybank, context={"request": request})
        return Response({"error": False, "message": "Single company bank data fetched", "data": serializer.data})

    def update(self, request, pk=None):
        try:
            queryset = CompanyBank.objects.all()
            companybank = get_object_or_404(queryset, pk=pk)

            serializer = CompanyBankSerializer(
                companybank, data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            response_dict = {"error": False,
                             "message": "Company Bank Data updated successfully"}
        except:
            response_dict = {
                "error": False, "message": "Company Bank Data Did not update successfully"}
        return Response(response_dict)


class CompanyNameViewSet(generics.ListAPIView):
    serializer_class = CompanySerializer

    def get_queryset(self):
        name = self.kwargs['name']
        return Company.objects.filter(name=name)

class MedicineViewSet(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def create(self,request):
        try:
            serializer=MedicineSerializer(data=request.data,context={"request":request})
            serializer.is_valid(raise_exception=True)
            serializer.save()

            medicine_id=serializer.data['id']
            #Access The Serializer Id Which JUSt SAVE in OUR DATABASE TABLE
            #print(medicine_id)

            #Adding and Saving Id into Medicine Details Table
            medicine_details_list=[]
            for medicine_detail in request.data["medicine_details"]:
                print(medicine_detail)
                #Adding medicine id which will work for medicine details serializer
                medicine_detail["medicine_id"]=medicine_id
                medicine_details_list.append(medicine_detail)
                print(medicine_detail)

            serializer2=MedicalDetailsSerializer(data=medicine_details_list,many=True,context={"request":request})
            serializer2.is_valid()
            serializer2.save()

            dict_response={"error":False,"message":"Medicine Data Save Successfully"}
        except:
            dict_response={"error":True,"message":"Error During Saving Medicine Data"}
        return Response(dict_response)

    def list(self,request):
        medicine=Medicine.objects.all()
        serializer=MedicineSerializer(medicine,many=True,context={"request":request})

        medicine_data=serializer.data
        newmedicinelist=[]

        #Adding Extra Key for Medicine Details in Medicine
        for medicine in medicine_data:
            #Accessing All the Medicine Details of Current Medicine ID
            medicine_details=MedicalDetails.objects.filter(medicine_id=medicine["id"])
            medicine_details_serializers=MedicalDetailsSerializer(medicine_details,many=True)
            medicine["medicine_details"]=medicine_details_serializers.data
            newmedicinelist.append(medicine)

        response_dict={"error":False,"message":"All Medicine List Data","data":newmedicinelist}
        return Response(response_dict)

    def retrieve(self,request,pk=None):
        queryset=Medicine.objects.all()
        medicine=get_object_or_404(queryset,pk=pk)
        serializer=MedicineSerializer(medicine,context={"request":request})

        serializer_data=serializer.data
        # Accessing All the Medicine Details of Current Medicine ID
        medicine_details = MedicalDetails.objects.filter(medicine_id=serializer_data["id"])
        medicine_details_serializers = MedicalDetailsSerializer(medicine_details, many=True)
        serializer_data["medicine_details"] = medicine_details_serializers.data

        return Response({"error":False,"message":"Single Data Fetch","data":serializer_data})

    def update(self,request,pk=None):
        queryset=Medicine.objects.all()
        medicine=get_object_or_404(queryset,pk=pk)
        serializer=MedicineSerializer(medicine,data=request.data,context={"request":request})
        serializer.is_valid()
        serializer.save()
        #print(request.data["medicine_details"])
        for salt_detail in request.data["medicine_details"]:
            if salt_detail["id"]==0:
                #For Insert New Salt Details
                del salt_detail["id"]
                salt_detail["medicine_id"]=serializer.data["id"]
                serializer2 = MedicalDetailsSerializer(data=salt_detail,context={"request": request})
                serializer2.is_valid()
                serializer2.save()
            else:
                #For Update Salt Details
                queryset2=MedicalDetails.objects.all()
                medicine_salt=get_object_or_404(queryset2,pk=salt_detail["id"])
                del salt_detail["id"]
                serializer3=MedicalDetailsSerializer(medicine_salt,data=salt_detail,context={"request":request})
                serializer3.is_valid()
                serializer3.save()
                print("UPDATE")

        return Response({"error":False,"message":"Data Has Been Updated"})



# class MedicineViewSet(viewsets.ViewSet):
#     authentication_classes = [JWTAuthentication, ]
#     permission_classes = [IsAuthenticated]

#     def list(self, request):
#         medicine = Medicine.objects.all()
#         serializer = MedicineSerializer(
#             medicine, many=True, context={"request": request})
#         medicine_data=serializer.data
#         newmedicinelist=[]
#         for medicine in medicine_data:
#             medicine_details=MedicalDetails.objects.filter(medicine_id=medicine["id"])
#             medicine_details_serializers=MedicalDetailsSerializer(medicine_details,many=True)
#             medicine['medicine_details']=medicine_details_serializers.data
#             newmedicinelist.append(medicine)

#         response_dict = {
#             "error": False, "message": "medicine List Data", "data": newmedicinelist}
#         return Response(response_dict)

#     def create(self, request):
#         try:
#             serializer = MedicineSerializer(
#                 data=request.data, context={"request": request})
#             serializer.is_valid(raise_exception=True)
#             serializer.save()
#             medicine_id=serializer.data['id']
#             # print(medicine_id)
#             # access the serializer id which is just saved

#             medicine_details_list=[]
#             for medicine_detail in request.data['medicine_details']:
#                 # adding medicine id to the medicine details list
#                 medicine_detail['medicine_id']=medicine_id
#                 medicine_details_list.append(medicine_detail)
#             serializer2=MedicalDetailsSerializer(data=medicine_details_list,many=True,context={"request":request})
#             serializer2.is_valid(raise_exception=True)
#             serializer2.save()
#             response_dict = {"error": False,
#                              "message": "medicine Data Saved Successfully"}
#         except:
#             response_dict = {"error": False,
#                              "message": "Error. Couldn't save data"}
#         return Response(response_dict)

#     def update(self, request, pk=None):
#         try:
#             queryset = Medicine.objects.all()
#             medicine = get_object_or_404(queryset, pk=pk)
#             serializer = MedicineSerializer(
#                 medicine, data=request.data, context={"request", request})
#             serializer.is_valid(raise_exception=True)
#             serializer.save()
#             response_dict = {"error": False,
#                              "message": "medicine data updated successfully"}

#         except:
#             response_dict = {"error": False, "message": "Error while updating"}
#         return Response(response_dict)

    # company_list = CompanyViewSet.as_view({"get": "list"})
    # company_create = CompanyViewSet.as_view({"post": "create"})
    # company_update = CompanyViewSet.as_view({"put": "update"})
