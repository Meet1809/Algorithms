
<!DOCTYPE html>
<html>
   <head>
     <meta charset="utf-8">
     <meta name="viewport" content="width=device-width,intial-scale=1.0">
     <title>Insertion Sort</title>
    <?php include "MasterTemplate/files.php" ?>
   </head>
   <body class="body-class">
       <?php include "navigation/navigation.php"?>
    <div class="main-div">
      <h1>Insertion Sort</h1>
      <div class="content">
        <script src="https://gist.github.com/Bhagydeep24/5a9f8293d0973c21173d7c1ae5969897.js"></script>
        </br></br>
        <article class="">
        Insertion sort is a simple sorting algorithm. And one would have used and implemented it atleast once in their life while playing cards.
        The person makes a fan of cards then starts sorting it from leftside. It moves to right and pick the card and insert it in correct
        position where left side is already sorted. It keeps picking the card from right and insert in left part until all cards are sorted.
        </br></br>
        <h3>How it works:</h3>
        </br>
        Let's suppose we use integer array as an input. Insertion sort uses 2 loops. First, loop is where key is assigned and it
        keeps on iterating to right. Key is matched to exact right element and if key is greater than right element then that element is
        picked and inserted in correct position on left side. And to do the later part second loop is used where space for new element is made
        for new element and it done by shifting the elements to the right until correct position for new element is found.
        For better understanding let's take an array of 5 element [5, 4, 3, 2, 1].
        </br></br>
        <i>For key index=0,</i>
        </br>
        <pre>
        5 & 4 are compared and since 5 is greater than 4,
        4 is insert ahead of 5 by moving 5 to right
        and 4 is placed on 5's position.
        </pre>
        <i>For key index=1,</i>
        </br>
        <pre>
        5 & 3 are compared and since 5 is greater than 3,
        3 is insert ahead of 5 by moving 5 to right and 3 is placed on 5's position.
        But 4 is greater than 3,so 3 is insert ahead of 4 by moving 4 to right
        and 3 is placed on 4's position.
        </pre>
        <i>For key index=2,</i>
        </br>
        <pre>
        5 & 2 are compared and since 5 is greater than 2,
        2 is insert ahead of 5 by moving 5 to right and 2 is placed on 5's position.
        But 4 is greater than 2,so 2 is insert ahead of 4 by moving 4 to right
        and 2 is placed on 4's position.
        But again 3 is greater than 2,so 2 is insert ahead of 3 by moving 3 to right
        and 2 is placed on 3's position.
        </pre>
        <i>For key index=3,</i>
        </br>
        <pre>
        5 & 1 are compared and since 5 is greater than 1,
        1 is insert ahead of 5 by moving 5 to right and 1 is placed on 5's position.
        But 4 is greater than 1,so 1 is insert ahead of 4 by moving 4 to right
        and 1 is placed on 4's position. But again
        3 is greater than 1,so 1 is insert ahead of 3 by moving 3 to right
        and 1 is placed on 3's position.
        But again 1 is greater than 1,so 1 is insert ahead of 2 by moving 2 to right
        and 1 is placed on 2's position.
        </pre>
        </br>
        <h3>Sorted Array:</h3>
        We have achieved our solution and finally the array achieved is [1, 2, 3, 4, 5].
        </br></br>
        <h3>Not a Stable Sorting Algorithm:</h3>
        Insertion sort is not a stable algorithm means if there is a duplicate element then these two duplicate elements are might swap their places.
        For example we have an array [2, 1, 8, 6, 8, 3]. Here we have 8 as a duplicate element in our array and to show the difference
        we can mark 2nd 8 with * which makes our array look like [2, 1, 8, 6, 8*, 3]. After applying insertion sorting the array we achieved is
        [1, 2, 3, 6, 8*, 8]. And it can be seen our marked element came before original 8.
        </br></br>
        <h3>In Place Sorting Algorithm:</h3>
        Insertion sort is a in place algorithm means we never used and extra array for storage and all our elements just swaped their position. Therefore space
        complexity of insertion sort is O(1).
        </br></br>
        <h3>Time complexity:</h3>
        Time complexity of insertion sort is O(n<sup>2</sup>).
        Worst case and average case both is O(n<sup>2</sup>) because in both case both loops are going to iterate so our time complexity
        is n times*n times. Whereas in best case time complexity is O(n) in a situation where our array is almost sorted.
        </br></br>
        <h3>Pros:</h3>
        It can be used in a situation where our array is almost sorted.
        </br></br>
        <h3>Cons:</h3>
        Like Bubble Sort we cannot use insertion sort where array size is huge and it is totally unsorted because time complety increases with n<sup>2</sup>.
        </br></br>
        <h3>Code Editor:</h3>
        </br>
        Here is our code interpreter, code is already written in python we can execute the code by clicking on play button. After that we can input
        our own array string separated by comma.
      </br></br>
      Array string in case don't won't to waste time: 679,49,-1,455,3. After copy pasting array just press enter and output will display how the
      whole array is sorted with each step.
      </br></br>
      Execution time in seconds is also return with which we can observe execution time of the algorithm.
      <br
    </br></br>
      <iframe src="https://trinket.io/embed/python/9ac2e5b6ba" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>    </div>
    </div>

   </body>
</html>
