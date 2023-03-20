import {describe, expect, it} from "vitest";
import {concatenatePath} from "../concatenatePath";

describe('Concatenate path api util', () => {
    it('Passed single path', () => {
        expect(concatenatePath('/api/hello')).toBe('/api/hello')
        expect(concatenatePath('api/hello')).toBe('/api/hello')
    })

    it('Passed two arguments', () => {
        expect(concatenatePath('/api/', 'hello')).toBe('/api/hello')
        expect(concatenatePath('api', 'hello')).toBe('/api/hello')
    })
})
