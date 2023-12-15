<?php

use PHPUnit\Framework\TestCase;

class ArraySortTest extends TestCase
{
    public function testFirstAndLastElementsAreDifferentAfterSorting()
    {
        // Crear un array de 100 números falsos
        $numbers = $this->fakeArrayOfNumbers(100);

        // Obtener el primer y último elemento antes de la ordenación
        $firstElementBeforeSorting = $numbers[0];
        $lastElementBeforeSorting = end($numbers);

        // Ordenar el array
        sort($numbers);

        // Obtener el primer y último elemento después de la ordenación
        $firstElementAfterSorting = $numbers[0];
        $lastElementAfterSorting = end($numbers);

        // Verificar que el primer y último elemento antes y después de la ordenación son diferentes
        $this->assertNotEquals($firstElementBeforeSorting, $firstElementAfterSorting);
        $this->assertNotEquals($lastElementBeforeSorting, $lastElementAfterSorting);
    }

    // Función para crear un array de números falsos
    private function fakeArrayOfNumbers($count)
    {
        $numbers = [];
        for ($i = 0; $i < $count; $i++) {
            $numbers[] = mt_rand(1, 1000);
        }
        return $numbers;
    }
}
