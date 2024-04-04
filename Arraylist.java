/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Project/Maven2/JavaApp/src/main/java/${packagePath}/${mainClassName}.java to edit this template
 */

package com.mycompany.arraylist;

import java.util.ArrayList;

public class Arraylist {
 public static void main(String[] args) {
     
       int cero[] = {};
       for (int e=0;e<cero.length;e++){
           System.out.println(cero[0]);
           System.out.println(cero.length);
       }
   
 int cinco[] = {5,25,30,35,40,45,50};  
ArrayList<Integer> list = new ArrayList();
     System.out.println(cinco[2]);
     
     for (int i=0;i<cinco.length;i++){
             System.out.println(cinco[i]);
     }
     System.out.println("Primer elemento:  "+ cinco[0]);
     System.out.println("Segundo elemento:  "+ cinco[3]);
     System.out.println("Tercer elemento:  "+ cinco[6]);
     
    {
      ArrayList<String> Datos_personales = new ArrayList();
      Datos_personales.add("Jesus");
      Datos_personales.add("18");
      Datos_personales.add("1.85");
      Datos_personales.add("Soltero");
      Datos_personales.add("Blas de lezo");
      Datos_personales.add("Parentesco");
      System.out.println("Datos personales: "+ Datos_personales);
    
 }
 

   ArrayList<String> it_companies = new ArrayList();
   it_companies.add("Facebook");
   it_companies.add("IBM");
   it_companies.add("google");
   it_companies.add("Microsoft");
   it_companies.add("Apple");
   it_companies.add("Oracle");
   it_companies.add("Amazon");
   it_companies.add("Afinia");
     System.out.println("Empresas: "+it_companies);
    boolean existeEmpresa = it_companies.contains("Facebook");
     System.out.println("Existe Facebook en la lista? "+ existeEmpresa);
     System.out.println("El tamaño de la lista es: "+ it_companies.size());
     System.out.println("Lista invertida: "+ it_companies.reversed());
     it_companies.remove("Afinia");
     System.out.println("Lista con el elemento eliminado"+ it_companies );
     it_companies.clear();
     System.out.println("Lista limpiada:"+ it_companies );
 }
     }
             
        
    


