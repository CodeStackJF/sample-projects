<?php
/** @var \Laravel\Boost\Install\GuidelineAssist $assist */
?>
___SCOPED_START_WyJ0ZXN0c1wvKioiXQ==___
## Pest

- This project uses Pest for testing. Create tests: ___SINGLE_BACKTICK___<?php echo e($assist->artisanCommand('make:test --pest {name}')); ?>___SINGLE_BACKTICK___.
- The ___SINGLE_BACKTICK___{name}___SINGLE_BACKTICK___ argument should not include the test suite directory. Use ___SINGLE_BACKTICK___<?php echo e($assist->artisanCommand('make:test --pest SomeFeatureTest')); ?>___SINGLE_BACKTICK___ instead of ___SINGLE_BACKTICK___<?php echo e($assist->artisanCommand('make:test --pest Feature/SomeFeatureTest')); ?>___SINGLE_BACKTICK___.
- Run tests: ___SINGLE_BACKTICK___<?php echo e($assist->artisanCommand('test --compact')); ?>___SINGLE_BACKTICK___ or filter: ___SINGLE_BACKTICK___<?php echo e($assist->artisanCommand('test --compact --filter=testName')); ?>___SINGLE_BACKTICK___.
- Do NOT delete tests without approval.
___SCOPED_END___
<?php /**PATH D:\josej\Documents\Proyectos\ExamenDeGrado\C#\php\ugb\storage\framework\views/cf2b5272300017a55d791a9e1c44afb7.blade.php ENDPATH**/ ?>