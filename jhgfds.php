<?php 

function findSubarrays( $arr, $n) 
{ 
    $found = false; 
    $lsum = 0; 
    for ( $i = 0; $i < $n - 1; $i++) 
    { 
        $lsum += $arr[$i]; 
        $rsum = 0; 
        for ( $j = $i + 1; $j < $n; $j++) 
            $rsum += $arr[$j]; 
  
         
        if ($lsum * ($n - $i - 1) ==  
                $rsum * ($i + 1)) 
        { 
        echo "From ( 0 ", $i," )". 
             " to (", $i + 1," ", $n - 1,")\n"; 
                                              
            $found = true; 
        } 
    } 
  
   
    if ($found == false) 
        echo "Subarrays not found" ; 
} 
  

$arr = array(1, 5, 7, 2, 0); 
$n = count($arr); 
findSubarrays($arr, $n); 
